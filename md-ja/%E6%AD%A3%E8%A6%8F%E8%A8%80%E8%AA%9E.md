# 正規言語

**正規言語**（せいきげんご）または**正則言語**（せいそくげんご）は、以下に示す性質（いずれも等価）を満たす[形式言語](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E8%A8%80%E8%AA%9E "形式言語")である。

- [決定性有限オートマトン](https://ja.wikipedia.org/wiki/%E6%B1%BA%E5%AE%9A%E6%80%A7%E6%9C%89%E9%99%90%E3%82%AA%E3%83%BC%E3%83%88%E3%83%9E%E3%83%88%E3%83%B3 "決定性有限オートマトン")によって受理可能
- [非決定性有限オートマトン](https://ja.wikipedia.org/wiki/%E9%9D%9E%E6%B1%BA%E5%AE%9A%E6%80%A7%E6%9C%89%E9%99%90%E3%82%AA%E3%83%BC%E3%83%88%E3%83%9E%E3%83%88%E3%83%B3 "非決定性有限オートマトン")によって受理可能
- [正規表現](https://ja.wikipedia.org/wiki/%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE "正規表現")で記述可能
- [正規文法](https://ja.wikipedia.org/wiki/%E6%AD%A3%E8%A6%8F%E6%96%87%E6%B3%95 "正規文法")から生成可能
- 読みとり専用[チューリングマシン](https://ja.wikipedia.org/wiki/%E3%83%81%E3%83%A5%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%9E%E3%82%B7%E3%83%B3 "チューリングマシン")で受理可能

## 定義

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E6%AD%A3%E8%A6%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=1 "節を編集: 定義")]

文字セット Σ 上の正規言語の集合は以下のように再帰的に定義される。

- 空の言語 0 は正規言語である。
- 空文字列言語 { ε } は正規言語である。
- *a* ∈ Σ である各 *a* について、それだけを含む[単集合](https://ja.wikipedia.org/wiki/%E5%8D%98%E9%9B%86%E5%90%88 "単集合")言語 { *a* } は正規言語である。
- *A* と *B* が正規言語であるとき、*A* ∪ *B*（和集合）も *A* • *B*（結合）も *A*\*（[クリーネ閉包](https://ja.wikipedia.org/wiki/%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%8D%E9%96%89%E5%8C%85 "クリーネ閉包")）も正規言語である[\[1\]](https://ja.wikipedia.org/wiki/#cite_note-1)。
- それ以外の Σ 上の言語は正規言語ではない。

有限の文字列から構成される言語は全て正規言語である。その他の典型的な例としては、文字セット {*a*, *b*} を使った文字列のうち、偶数個の *a* を含む文字列の集まりは正規言語であるし、任意個数の *a* の後に任意個数の *b* が続く文字列で構成される言語も正規言語である。

## 閉包属性

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E6%AD%A3%E8%A6%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=2 "節を編集: 閉包属性")]

正規言語に対して、和集合、積集合、差集合といった演算を施した結果も正規言語である。正規言語の補集合（文字セットから生成される全文字列を全体集合とする）も正規言語である。正規言語の文字列を全て逆転させたものも正規言語である。正規言語の連結（ふたつの言語に含まれる文字列をあらゆる組み合わせで連結した文字列の集合）をしたものも正規言語である。「シャッフル」をふたつの正規言語に施した結果も正規言語である。正規言語と任意の言語の商集合も正規言語である。個々の操作の具体的意味については[形式言語#定義](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E8%A8%80%E8%AA%9E#%E5%AE%9A%E7%BE%A9 "形式言語")を参照されたい。

## ある言語が正規言語であるかどうかの判断基準

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E6%AD%A3%E8%A6%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=3 "節を編集: ある言語が正規言語であるかどうかの判断基準")]

[チョムスキー階層](https://ja.wikipedia.org/wiki/%E3%83%81%E3%83%A7%E3%83%A0%E3%82%B9%E3%82%AD%E3%83%BC%E9%9A%8E%E5%B1%A4 "チョムスキー階層")での正規言語の位置によれば、正規言語は[文脈自由言語](https://ja.wikipedia.org/wiki/%E6%96%87%E8%84%88%E8%87%AA%E7%94%B1%E8%A8%80%E8%AA%9E "文脈自由言語")の[真部分集合](https://ja.wikipedia.org/wiki/%E9%83%A8%E5%88%86%E9%9B%86%E5%90%88 "部分集合")である。すなわち、正規言語は文脈自由言語に含まれる一方、その逆は真ではない。

例えば、同じ個数の *a* と *b* を含む文字列から成る言語は文脈自由言語ではあるが、正規言語ではない。このような言語が正規言語ではないことを証明するには、[マイヒル-ネローデの定理](https://ja.wikipedia.org/wiki/%E3%83%9E%E3%82%A4%E3%83%92%E3%83%AB-%E3%83%8D%E3%83%AD%E3%83%BC%E3%83%87%E3%81%AE%E5%AE%9A%E7%90%86 "マイヒル-ネローデの定理")か[反復補題](https://ja.wikipedia.org/wiki/%E6%AD%A3%E8%A6%8F%E8%A8%80%E8%AA%9E%E3%81%AE%E5%8F%8D%E5%BE%A9%E8%A3%9C%E9%A1%8C "正規言語の反復補題") (pumping lemma) を使う。

正規言語を代数学的に定義するには、二つの方法がある。Σ を有限のアルファベットとし、Σ\* を Σ 上の[自由モノイド](https://ja.wikipedia.org/w/index.php?title=%E8%87%AA%E7%94%B1%E3%83%A2%E3%83%8E%E3%82%A4%E3%83%89\&action=edit\&redlink=1 "自由モノイド (存在しないページ)")（Σ によって作られる記号列全て）とすると、*f* : Σ\* → *M* は[モノイド同型](https://ja.wikipedia.org/w/index.php?title=%E3%83%A2%E3%83%8E%E3%82%A4%E3%83%89%E5%90%8C%E5%9E%8B\&action=edit\&redlink=1 "モノイド同型 (存在しないページ)")となる。ただしここで *M* は*有限*のモノイドである。そして、*S* を *M* の部分集合とすると、*f*−1(*S*) は正規言語となる。任意の正規言語はこのようにして構成することができる。

もう一つの方法として、*L* が Σ 上の言語であるとき、Σ\* 上の[同値関係](https://ja.wikipedia.org/wiki/%E5%90%8C%E5%80%A4%E9%96%A2%E4%BF%82 "同値関係") \~ を次のように定義する。

- ![{\displaystyle x\sim y:\Leftrightarrow \forall z\in \Sigma ^{\*}:xz\in L\leftrightarrow yz\in L}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f9db5e9f8010e9b0e4c1aee75dc5781f696fb7fe)

すると、*L* が正規言語であることは、同値関係 \~ の作る同値類の指標（濃度）が有限であることと[同値](https://ja.wikipedia.org/wiki/%E5%90%8C%E5%80%A4 "同値")になる。そして、同値類の指標は *L* を受理する最小の決定性有限オートマトンの状態の個数に一致する。

## 脚注

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E6%AD%A3%E8%A6%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=4 "節を編集: 脚注")]

\[[脚注の使い方](https://ja.wikipedia.org/wiki/Help:%E8%84%9A%E6%B3%A8/%E8%AA%AD%E8%80%85%E5%90%91%E3%81%91 "Help:脚注/読者向け")]

1. **[^](https://ja.wikipedia.org/wiki/#cite_ref-1)** つまり[正規演算](https://ja.wikipedia.org/w/index.php?title=%E6%AD%A3%E8%A6%8F%E6%BC%94%E7%AE%97\&action=edit\&redlink=1 "正規演算 (存在しないページ)")に[閉じている](https://ja.wikipedia.org/wiki/%E9%96%89%E3%81%98%E3%81%A6%E3%81%84%E3%82%8B "閉じている")。

<!-- 
NewPP limit report
Parsed by mw‐web.eqiad.main‐55d995bd96‐c58j8
Cached time: 20250117151337
Cache expiry: 2592000
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.014 seconds
Real time usage: 0.052 seconds
Preprocessor visited node count: 91/1000000
Post‐expand include size: 367/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 5/100
Expensive parser function count: 0/500
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 366/5000000 bytes
Number of Wikibase entities loaded: 0/400
-->

<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    4.526      1 -total
 59.04%    2.672      1 Template:Reflist
 38.42%    1.739      1 Template:脚注ヘルプ
-->

<!-- Saved in parser cache with key jawiki:pcache:66:|#|:idhash:canonical and timestamp 20250117151337 and revision id 93928748. Rendering was triggered because: page-view
 -->
