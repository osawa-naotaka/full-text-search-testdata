import { unified } from 'unified'
import rehypeParse from 'rehype-parse'
import rehypeRemark from 'rehype-remark'
import remarkStringify from 'remark-stringify'
import remarkParse from 'remark-parse'
import stripMarkdown from 'strip-markdown'
import remarkGfm from 'remark-gfm'
import type { Options } from 'remark-stringify'
import { promises as fs } from 'fs'
import path from 'path'

/**
 * HTMLをGitHub Flavored Markdownに変換します
 * 
 * @param html - 変換するHTML文字列
 * @returns 変換されたMarkdown文字列
 */
export async function html2md(html: string): Promise<string> {
  const stringifyOptions: Options = {
    bullet: '-',
    rule: '-',
    listItemIndent: 'one'
  }

  const file = await unified()
    // HTMLをパース
    .use(rehypeParse)
    // rehypeからremarkに変換
    .use(rehypeRemark)
    // GFMの機能を有効化
    .use(remarkGfm)
    // Markdownとして文字列化
    .use(remarkStringify, stringifyOptions)
    .process(html)

  return String(file)
}

/**
 * MarkdownをPlain textに変換します
 * 
 * @param markdown - 変換するMarkdown文字列
 * @returns 変換されたPlain text文字列
 */
export async function md2plain(markdown: string): Promise<string> {
  const file = await unified()
    // Markdownをパース
    .use(remarkParse)
    // Markdownの装飾を除去
    .use(stripMarkdown)
    // 文字列として出力
    .use(remarkStringify)
    .process(markdown)

  return String(file).trim()
}

/**
 * JSONファイルを読み込みます
 * 
 * @param filePath - 読み込むJSONファイルのパス
 * @returns パースされたJSONオブジェクト
 * @throws JSONファイルの読み込みに失敗した場合
 */
export async function readJsonFile<T>(filePath: string): Promise<T> {
  try {
    const jsonString = await fs.readFile(filePath, 'utf-8')
    return JSON.parse(jsonString) as T
  } catch (error) {
    if (error instanceof Error) {
      throw new Error(`JSONファイルの読み込みに失敗しました: ${error.message}`)
    } else {
      throw new Error(`JSONファイルの読み込みに失敗しました: 不明なエラー`)
    }
  }
}

/**
 * ファイルを書き込みます
 * 
 * @param filePath - 書き込み先のファイルパス
 * @param htmlContent - 書き込む文字列
 * @throws ファイルの書き込みに失敗した場合
 */
export async function writeFile(filePath: string, htmlContent: string): Promise<void> {
  try {
    await fs.mkdir(path.dirname(filePath), { recursive: true })
    await fs.writeFile(filePath, htmlContent, 'utf-8')
  } catch (error) {
    if (error instanceof Error) {
      throw new Error(`ファイルの書き込みに失敗しました: ${error.message}`)
    } else {
      throw new Error(`ファイルの書き込みに失敗しました: 不明なエラー`)
    }
  }
}

/**
 * 文字列をファイル名として安全な形式に変換します
 * 
 * @param title - 変換する文字列
 * @returns ファイル名として安全な文字列
 */
function sanitizeFileName(title: string): string {
  return encodeURIComponent(
    title
      .replace(/\s+/g, '-') // スペースをハイフンに変換
      .replace(/[\/\\:*?"<>|]/g, '_') // Windowsで使用できない文字を削除
  )
}

async function main() {
  if (process.argv.length < 4) {
    console.error('使用方法: node script.js <入力JSONファイル> <出力ディレクトリ>');
    process.exit(1);
  }

  const inputFile = process.argv[2];
  const outputDir = process.argv[3];

  try {
    const json = await readJsonFile<{title: string, html: string}[]>(inputFile);

    for (const item of json) {
      const markdown = await html2md(item.html);
      const safeFileName = sanitizeFileName(item.title);
      await writeFile(path.join(outputDir, safeFileName + '.md'), markdown);
    }
    console.log('変換が完了しました');
  } catch (error) {
    if (error instanceof Error) {
      console.error('エラーが発生しました:', error.message);
    } else {
      console.error('不明なエラーが発生しました');
    }
    process.exit(1);
  }
}

main();

