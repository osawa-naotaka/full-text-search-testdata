import json
import random
import MeCab
import re
from collections import Counter
import unicodedata
from typing import List, Dict
import argparse

class KeywordExtractor:
    def __init__(self, lang: str):
        self.lang = lang
        # 言語ごとの設定
        self.configs = {
            "ja": {
                "target_pos": ["名詞"],  # 抽出対象の品詞
                "exclude_pos": ["非自立", "代名詞", "数"],  # 除外する品詞細分類
                "min_length": 2,  # 最小文字数
            },
            "en": {
                "min_length": 3,  # 英語は3文字以上を対象
            }
        }
        self.config = self.configs.get(lang, {"min_length": 2})
        
        if lang == "ja":
            self.mecab = MeCab.Tagger("-d /nix/store/m59581a7n90qrf6b81cfww2g485gqa0h-python3.12-unidic-lite-1.0.8/lib/python3.12/site-packages/unidic_lite/dicdir/")
    
    def clean_text(self, text: str) -> str:
        """ウィキテキストからプレーンテキストを抽出"""
        # テンプレート、参照、HTMLタグの除去
        text = re.sub(r'\{\{[^\}]*\}\}', '', text)
        text = re.sub(r'<[^>]*>', '', text)
        text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text)
        text = re.sub(r'==.*?==', '', text)
        text = re.sub(r'\'\'\'?.*?\'\'\'?', '', text)
        # 余分な空白と改行の整理
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def extract_japanese_keywords(self, text: str, min_freq: int = 2) -> List[str]:
        """日本語テキストからキーワードを抽出"""
        keywords = []
        node = self.mecab.parseToNode(text)
        
        while node:
            features = node.feature.split(',')
            if len(features) >= 1:
                pos = features[0]
                
                # 品詞フィルタリング
                if pos in self.config["target_pos"]:
                    word = node.surface
                    # 除外条件のチェック
                    if (len(word) >= self.config["min_length"] and
                        not any(ex in features for ex in self.config["exclude_pos"]) and
                        not word.isdigit() and
                        not all(unicodedata.category(c).startswith('P') for c in word)):
                        keywords.append(word)
            node = node.next
        
        # 頻出度でフィルタリング
        counter = Counter(keywords)
        return [word for word, count in counter.items() if count >= min_freq]
    
    def extract_english_keywords(self, text: str, min_freq: int = 2) -> List[str]:
        """英語テキストからキーワードを抽出"""
        # 単語の抽出（簡易的な実装）
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        # ストップワードの除去（必要に応じて拡張）
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        words = [w for w in words if len(w) >= self.config["min_length"] and w not in stop_words]
        
        # 頻出度でフィルタリング
        counter = Counter(words)
        return [word for word, count in counter.items() if count >= min_freq]
    
    def extract_keywords(self, text: str, min_freq: int = 2) -> List[str]:
        """言語に応じたキーワード抽出"""
        text = self.clean_text(text)
        if self.lang == "ja":
            return self.extract_japanese_keywords(text, min_freq)
        else:
            return self.extract_english_keywords(text, min_freq)

def main():
    parser = argparse.ArgumentParser(description='Extract keywords from Wikipedia articles')
    parser.add_argument('input_file', help='Input JSON file path')
    parser.add_argument('--lang', default='ja', help='Language code (default: ja)')
    parser.add_argument('--keywords-per-article', type=int, default=5, help='Number of keywords to extract per article')
    parser.add_argument('--min-freq', type=int, default=2, help='Minimum frequency for keywords')
    parser.add_argument('--output', help='Output file path (optional)')
    args = parser.parse_args()

    # JSONファイルの読み込み
    with open(args.input_file, 'r', encoding='utf-8') as f:
        articles = json.load(f)
    
    extractor = KeywordExtractor(args.lang)
    results = []
    
    for article in articles:
        title = article['title']
        content = article['content']
        
        # キーワード抽出
        all_keywords = extractor.extract_keywords(content, args.min_freq)
        
        # ランダムに指定数選択
        if all_keywords:
            selected_keywords = random.sample(
                all_keywords,
                min(args.keywords_per_article, len(all_keywords))
            )
        else:
            selected_keywords = []
        
        result = {
            "title": title,
            "keywords": selected_keywords
        }
        results.append(result)
        
        # 進捗表示
        print(f"Processed: {title}")
        print(f"Keywords: {', '.join(selected_keywords)}\n")
    
    # 結果の保存
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    
if __name__ == "__main__":
    main()
