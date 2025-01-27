# 形式言語

**形式言語**（けいしきげんご、[英](https://ja.wikipedia.org/wiki/%E8%8B%B1%E8%AA%9E "英語"): formal language）とは、[文法](https://ja.wikipedia.org/wiki/%E6%96%87%E6%B3%95 "文法")や[構文](https://ja.wikipedia.org/wiki/%E6%A7%8B%E6%96%87 "構文"), [統語論](https://ja.wikipedia.org/wiki/%E7%B5%B1%E8%AA%9E%E8%AB%96 "統語論")などが、すべて形式的に与えられている[言語](https://ja.wikipedia.org/wiki/%E8%A8%80%E8%AA%9E "言語")である。[人工言語](https://ja.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E8%A8%80%E8%AA%9E "人工言語")の一種[\[1\]](https://ja.wikipedia.org/wiki/#cite_note-1)。

→「[形式体系](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E4%BD%93%E7%B3%BB "形式体系")」も参照

形式的でないために、しばしば曖昧さが残されたり、話者集団によって用法がうつろいていったりする[自然言語](https://ja.wikipedia.org/wiki/%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E "自然言語")に対して、形式言語は、用法の変化に関しては非常に厳格である。

この記事では、形式的な統語論すなわち構文の形式的な定義と[形式文法](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%96%87%E6%B3%95 "形式文法")について述べる。形式的な意味論については[形式意味論](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%84%8F%E5%91%B3%E8%AB%96 "形式意味論")の記事を参照。

## 定義

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E5%BD%A2%E5%BC%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=1 "節を編集: 定義")]

形式言語の理論、特に[オートマトン理論](https://ja.wikipedia.org/wiki/%E3%82%AA%E3%83%BC%E3%83%88%E3%83%9E%E3%83%88%E3%83%B3 "オートマトン")と関連したそれにおいては、言語は[アルファベット](https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%99%E3%83%83%E3%83%88_\(%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%A6\) "アルファベット (計算機科学)")の列（語 word） の集合である[\[2\]](https://ja.wikipedia.org/wiki/#cite_note-2)。

![{\displaystyle L\subset \Sigma ^{\*}=\\{\langle \sigma \_{1},\sigma \_{2},...\rangle |\sigma \_{i}\in \Sigma \\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/853d261f9aca42397cb084eec55c98a08c32ff90)

ただし、長さゼロの**空単語**（*Empty Word*, 記号 ![{\displaystyle e}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cd253103f0876afc68ebead27a5aa9867d927467)、![{\displaystyle \epsilon }](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3837cad72483d97bcdde49c85d3b7b859fb3fd2)、![{\displaystyle \Lambda }](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ac0a4a98a414e3480335f9ba652d12571ec6733)）も含む。 チューリングマシンの言語は単なる文字列なので、数学的構造(他のチューリングマシンを含む)を扱うには符号化([エンコード](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%89 "エンコード"))し、その数値を解釈するプログラムを埋め込む必要がある。 チューリング完全機械は十分強力なので、この手法であらゆる列挙可能な構造を扱うことができる。チューリングマシンの数値表現については(チューリングマシンの)表記(description)という。

あるチューリングマシンが存在して、言語に属するすべての語 *w* に対して動作させると受理状態で停止し、属さない語には受理しないようなとき、その言語は**チューリング認識可能**という。 また、言語に属さないときは必ず拒否状態で停止する場合、その言語は**チューリング判別可能**であるという。(この2つの違いは、一部の入力に対してチューリングマシンが停止しない場合があるかどうかである) また、チューリングマシン**TM**の言語 *L*(**TM**) とは、テープに *w* をセットしたあと、**TM**を動作させると受理状態に入って停止するような *w* の集合からなる言語(**TM**認識可能な言語)のことである。

この言語には以下のような演算が定義される。ここで、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) と ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) は共通のアルファベットから構成される言語であるとする。

- 「連結」![{\displaystyle L\_{1}L\_{2}\quad }](https://wikimedia.org/api/rest_v1/media/math/render/svg/672373692b198bda74d390ac471b75ad90ad11e6) は、文字列群 ![{\displaystyle vw}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8354a09980e3eb2de1a7d376cc69b544c43cced) から構成される。ここで、![{\displaystyle v}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e07b00e7fc0847fbd16391c778d65bc25c452597) は ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれる文字列で、![{\displaystyle w}](https://wikimedia.org/api/rest_v1/media/math/render/svg/88b1e0c8e1be5ebe69d18a8010676fa42d7961e6) は ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) に含まれる文字列である。
- 「積集合」![{\displaystyle L\_{1}\cap L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/159185961cf4ee1f5bcd827ae7efa311b81da905) は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) にも ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) にも含まれる文字列の集合である。
- 「和集合」![{\displaystyle L\_{1}\cup L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1f3ba91b5655b26d6dd518a902ac0aed95c1aca4) は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) か ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) に含まれる文字列の集合である。
- ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) の「補集合」は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれない全ての文字列の集合である。
- 「商集合」![{\displaystyle L\_{1}/L\_{2}\quad }](https://wikimedia.org/api/rest_v1/media/math/render/svg/b1cb6d6091babf386b828ec5c2c382968f861094) は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれる文字列 ![{\displaystyle vw}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8354a09980e3eb2de1a7d376cc69b544c43cced) に対して、![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) に含まれる文字列 ![{\displaystyle w}](https://wikimedia.org/api/rest_v1/media/math/render/svg/88b1e0c8e1be5ebe69d18a8010676fa42d7961e6) が存在するときに、全ての ![{\displaystyle v}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e07b00e7fc0847fbd16391c778d65bc25c452597) に相当する文字列群から構成される。
- 「[クリーネスター](https://ja.wikipedia.org/wiki/%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%8D%E3%82%B9%E3%82%BF%E3%83%BC "クリーネスター")」![{\displaystyle L\_{1}^{\*}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cae4218ec52d028f64543a0cefae5d48fdc526f0) は、![{\displaystyle w\_{1}w\_{2}...w\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/958f88f26bdb5017d239cc3153d9a31e21f05404) という形式の全文字列群から構成される。ただし、![{\displaystyle w\_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fe22f0329d3ecb2e1880d44d191aba0e5475db68) は ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれ、![{\displaystyle n\geq 0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ce8a1b7b3bc3c790054d93629fc3b08cd1da1fd0) である。注意すべきは、![{\displaystyle n=0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/26819344e55f5e671c76c07c18eb4291fcec85ae) の場合もあるので、空文字列 ![{\displaystyle \epsilon }](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3837cad72483d97bcdde49c85d3b7b859fb3fd2) も含まれるという点である。
- 「反転」![{\displaystyle L\_{1}^{R}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6166246702d7ddfc7706cd4d7db49cbe62b3da21) は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) の全文字列を反転させた文字列群から構成される。
- ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) と ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) の「シャッフル」とは、![{\displaystyle v\_{1}w\_{1}v\_{2}w\_{2}...v\_{n}w\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a6eb1abcd6c2ed7aec9a0cd932948056323b7319) で表される全文字列から構成される。ここで、![{\displaystyle n\geq 1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d8ce9ce38d06f6bf5a3fe063118c09c2b6202bfe) で、![{\displaystyle v\_{1},...,v\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ed315d96db6db7b0f8d128d1347e287935132df) を連結した ![{\displaystyle v\_{1}...v\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/44f8a5511a593e6302bd8ef1cfcbea378a567852) は ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれる文字列であり、![{\displaystyle w\_{1},...,w\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0b0d3622440fea8f79d0fbe7f49d9c8ac3953142) を連結した ![{\displaystyle w\_{1}...w\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e3990ba22d8e23e3ff1d36874469c17dbb1a2fd0) は ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) に含まれる文字列である。

[モデル理論](https://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%87%E3%83%AB%E7%90%86%E8%AB%96 "モデル理論")においては、言語は定数記号、関数記号、述語記号の集合である[\[3\]](https://ja.wikipedia.org/wiki/#cite_note-3)。

![{\displaystyle L=\\{c\_{0},c\_{1},...\\}\cup \\{f\_{0},f\_{1},...\\}\cup \\{p\_{0},p\_{1},...\\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/58fcb420669fabe7e0b41015b573d2e85e63d67b)

## 形式文法

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E5%BD%A2%E5%BC%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=2 "節を編集: 形式文法")]

→詳細は「[形式文法](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%96%87%E6%B3%95 "形式文法")」を参照

形式言語は、[形式文法](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%96%87%E6%B3%95 "形式文法")と密接な関係がある。例として、次のような[文脈自由文法](https://ja.wikipedia.org/wiki/%E6%96%87%E8%84%88%E8%87%AA%E7%94%B1%E6%96%87%E6%B3%95 "文脈自由文法")の構文規則があるとき、

- 名詞句 ::= 名詞 | 形容詞 名詞 | 名詞句 "を" 動詞 "ている" 名詞句
- 動詞 ::= "見"
- 名詞 ::= "猿" | "飼育員"
- 形容詞 ::= "小さい"

以下のように規則を再帰的に適用して、その言語の要素(名詞句)を列挙することができる。

1. (猿 飼育員 小さい猿 小さい飼育員)
2. (猿 飼育員 小さい猿 小さい飼育員 猿を見ている猿 猿を見ている飼育員 猿を見ている小さい猿 ... 小さい猿を見ている猿 ...)
3. (猿 飼育員 小さい猿 小さい飼育員 猿を見ている猿 ... 猿をみている猿を見ている猿 ... 小さい猿を見ている猿を見ている小さい飼育員を見ている猿 ...)

...

すなわち、このような操作の任意回の繰り返しによって、その言語(文の集合)が得られる。

また、形式文法が階層をなすという[チョムスキー階層](https://ja.wikipedia.org/wiki/%E3%83%81%E3%83%A7%E3%83%A0%E3%82%B9%E3%82%AD%E3%83%BC%E9%9A%8E%E5%B1%A4 "チョムスキー階層")は、生成する言語では言語の認識に必要な最小のオートマトンが階層をなすという形で現れる。

## その他

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E5%BD%A2%E5%BC%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=3 "節を編集: その他")]

|                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Twemoji12_1f50d.svg/38px-Twemoji12_1f50d.svg.png) | **この節には[独自研究](https://ja.wikipedia.org/wiki/Wikipedia:%E7%8B%AC%E8%87%AA%E7%A0%94%E7%A9%B6%E3%81%AF%E8%BC%89%E3%81%9B%E3%81%AA%E3%81%84 "Wikipedia:独自研究は載せない")が含まれているおそれがあります。** 問題箇所を[検証](https://ja.wikipedia.org/wiki/Wikipedia:%E6%A4%9C%E8%A8%BC%E5%8F%AF%E8%83%BD%E6%80%A7 "Wikipedia:検証可能性")し[出典を追加](https://ja.wikipedia.org/wiki/Wikipedia:%E5%87%BA%E5%85%B8%E3%82%92%E6%98%8E%E8%A8%98%E3%81%99%E3%82%8B "Wikipedia:出典を明記する")して、記事の改善にご協力ください。議論は[ノート](https://ja.wikipedia.org/wiki/%E3%83%8E%E3%83%BC%E3%83%88:%E5%BD%A2%E5%BC%8F%E8%A8%80%E8%AA%9E "ノート:形式言語")を参照してください。（2015年11月） |

### 言及される分野

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E5%BD%A2%E5%BC%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=4 "節を編集: 言及される分野")]

形式言語は、「人や[計算機](https://ja.wikipedia.org/wiki/%E8%A8%88%E7%AE%97%E6%A9%9F "計算機")の如何なる記号変換能力から如何なる[思考](https://ja.wikipedia.org/wiki/%E6%80%9D%E8%80%83 "思考")能力や[計算](https://ja.wikipedia.org/wiki/%E8%A8%88%E7%AE%97 "計算")能力が生まれるか」の学としての広義の[数理論理学](https://ja.wikipedia.org/wiki/%E6%95%B0%E7%90%86%E8%AB%96%E7%90%86%E5%AD%A6 "数理論理学")の研究対象であり、従って形式言語は、[哲学](https://ja.wikipedia.org/wiki/%E5%93%B2%E5%AD%A6 "哲学")・[言語学](https://ja.wikipedia.org/wiki/%E8%A8%80%E8%AA%9E%E5%AD%A6 "言語学")・[計算機科学](https://ja.wikipedia.org/wiki/%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%A6 "計算機科学")・[数学基礎論](https://ja.wikipedia.org/wiki/%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A4%8E%E8%AB%96 "数学基礎論")・[数理心理学](https://ja.wikipedia.org/wiki/%E6%95%B0%E7%90%86%E5%BF%83%E7%90%86%E5%AD%A6 "数理心理学")等々において重要な役割を演ずる。 それらの学問分野では、如何なる形式言語を研究すべきかの[文法論](https://ja.wikipedia.org/wiki/%E6%96%87%E6%B3%95 "文法")（構文論・統辞論）や形式言語の[意味論](https://ja.wikipedia.org/wiki/%E6%84%8F%E5%91%B3%E8%AB%96_\(%E6%9B%96%E6%98%A7%E3%81%95%E5%9B%9E%E9%81%BF\) "意味論 (曖昧さ回避)")や[演繹論](https://ja.wikipedia.org/wiki/%E6%BC%94%E7%B9%B9 "演繹")が研究される。

[形式手法](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%89%8B%E6%B3%95 "形式手法")という場合には、形式言語に加えて、模擬試験、検証・証明などの仕組みを込みで言う場合が有る。

### 自然言語への応用

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E5%BD%A2%E5%BC%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=5 "節を編集: 自然言語への応用")]

→「[生成文法](https://ja.wikipedia.org/wiki/%E7%94%9F%E6%88%90%E6%96%87%E6%B3%95 "生成文法")」および「[句構造文法](https://ja.wikipedia.org/wiki/%E5%8F%A5%E6%A7%8B%E9%80%A0%E6%96%87%E6%B3%95 "句構造文法")」を参照

[自然言語](https://ja.wikipedia.org/wiki/%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E "自然言語")を比較的単純な形式言語のモデルにあてはめて分析する言語学は、[チョムスキー](https://ja.wikipedia.org/wiki/%E3%83%8E%E3%83%BC%E3%83%A0%E3%83%BB%E3%83%81%E3%83%A7%E3%83%A0%E3%82%B9%E3%82%AD%E3%83%BC "ノーム・チョムスキー")によって提唱された。[音素](https://ja.wikipedia.org/wiki/%E9%9F%B3%E7%B4%A0 "音素")や[語幹](https://ja.wikipedia.org/wiki/%E8%AA%9E%E5%B9%B9 "語幹")などを素記号として考える。 実際の自然言語の[構文規則](https://ja.wikipedia.org/wiki/%E6%A7%8B%E6%96%87%E8%A6%8F%E5%89%87 "構文規則")（あるいは[文法](https://ja.wikipedia.org/wiki/%E6%96%87%E6%B3%95 "文法")）は、文字通り自然発生的のものであり、形式言語における構文規則のように明確に規定するのは難しい。

ただ、素朴な文法論の主張は、形式言語の理論とみなすことができる。 素朴な文法論は、例えば次のようなものである。

- [品詞](https://ja.wikipedia.org/wiki/%E5%93%81%E8%A9%9E "品詞")にはこのようなのものがある。
- この語はあの品詞に属す。
- この品詞に属す語をこの[活用](https://ja.wikipedia.org/wiki/%E6%B4%BB%E7%94%A8 "活用")と[組み合わせ](https://ja.wikipedia.org/wiki/%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B "組み合わせ")と[順序](https://ja.wikipedia.org/wiki/%E9%A0%86%E5%BA%8F "順序")とで並べると文（や[句](https://ja.wikipedia.org/wiki/%E5%8F%A5 "句")や[節](https://ja.wikipedia.org/wiki/%E7%AF%80_\(%E6%96%87%E6%B3%95\) "節 (文法)")）になる。

こういう文法論はすなわち、素記号とは何かを定め、それらから文を作る構文規則を定めるのだから、まさに形式言語の理論である。

こういう形式言語論的な文法論は、実際の言語と比較することで自然言語の特徴を浮き彫りにし、自然言語のより深い理解へと導くことを可能とすることもなくはない。言語そのものではなく、言語行動の深層をなす人間精神を探るためには、むしろこういう文法論を数学化し、更に[意味論](https://ja.wikipedia.org/wiki/%E6%84%8F%E5%91%B3%E8%AB%96_\(%E6%9B%96%E6%98%A7%E3%81%95%E5%9B%9E%E9%81%BF\) "意味論 (曖昧さ回避)")・文法論を伴った論理学にまで推し進めることが有意義ともいえよう。

## 脚注

\[[編集](https://ja.wikipedia.org/w/index.php?title=%E5%BD%A2%E5%BC%8F%E8%A8%80%E8%AA%9E\&action=edit\&section=6 "節を編集: 脚注")]

\[[脚注の使い方](https://ja.wikipedia.org/wiki/Help:%E8%84%9A%E6%B3%A8/%E8%AA%AD%E8%80%85%E5%90%91%E3%81%91 "Help:脚注/読者向け")]

1. **[^](https://ja.wikipedia.org/wiki/#cite_ref-1)** [言語学　その1\~当たり前過ぎて意識しなくなっていること](https://note.com/lincoln246/n/nc4002055d7b8)
2. **[^](https://ja.wikipedia.org/wiki/#cite_ref-2)** Micael Sipser (2005). *Introduction to the Theory of Computation*. [ISBN](https://ja.wikipedia.org/wiki/ISBN "ISBN") [0534950973](https://ja.wikipedia.org/wiki/%E7%89%B9%E5%88%A5:%E6%96%87%E7%8C%AE%E8%B3%87%E6%96%99/0534950973 "特別:文献資料/0534950973") 
3. **[^](https://ja.wikipedia.org/wiki/#cite_ref-3)** 坪井明人 (2011年). “[数学基礎論サマースクール モデル理論入門](http://www2.kobe-u.ac.jp/~kikyo/LogicSummerSchool2011/lectures/2011kobe_tsuboi.pdf)”. 2012年2月18日閲覧。

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png)

ウィキメディア・コモンズには、**[形式言語](https://commons.wikimedia.org/wiki/Category:Formal_languages?uselang=ja)**&#x306B;関連するカテゴリがあります。

| - [表](https://ja.wikipedia.org/wiki/Template:Logic "Template:Logic")
- [話](https://ja.wikipedia.org/w/index.php?title=Template%E2%80%90%E3%83%8E%E3%83%BC%E3%83%88:Logic\&action=edit\&redlink=1 "Template‐ノート:Logic (存在しないページ)")
- [編](https://ja.wikipedia.org/w/index.php?title=Template%3ALogic\&action=edit)
- [歴](https://ja.wikipedia.org/w/index.php?title=Template%3ALogic\&action=history)[論理学](https://ja.wikipedia.org/wiki/%E8%AB%96%E7%90%86%E5%AD%A6 "論理学")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - |
|  &#xA;関連項目&#xA;&#xA;&#xA;学術的領域	&#xA;議論学&#xA;価値論&#xA;批判的思考&#xA;再帰理論&#xA;形式意味論&#xA;論理史&#xA;非形式論理学&#xA;計算機科学における論理学（英語版）&#xA;数理論理学&#xA;数学&#xA;メタ論理学&#xA;メタ数学&#xA;モデル理論&#xA;哲学的論理学&#xA;哲学&#xA;論理学の哲学&#xA;数学の哲学&#xA;証明論&#xA;集合論&#xA;論理学の歴史&#xA;&#xA;基本概念	&#xA;アブダクション&#xA;分析的と総合的の区別（英語版）&#xA;二律背反&#xA;アプリオリ&#xA;演繹&#xA;定義(内包と外延)&#xA;記述&#xA;帰納&#xA;推論&#xA;論理的帰結&#xA;論理形式（英語版）&#xA;論理的含意（英語版）&#xA;論理的真理&#xA;名前&#xA;必要十分条件&#xA;意味&#xA;パラドックス&#xA;可能世界論&#xA;前提&#xA;確率&#xA;理性&#xA;推理&#xA;参考&#xA;意味論&#xA;命題&#xA;サブスティトゥーション（英語版）&#xA;統語論（英語版）&#xA;真理&#xA;真理値&#xA;妥当性&#xA;数学記号の表                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |   |
|  &#xA;哲学的論理学&#xA;&#xA;&#xA;批判的思考と非形式論理学	&#xA;分析&#xA;曖昧&#xA;信念&#xA;信用性（英語版）&#xA;根拠&#xA;説明&#xA;説明力（英語版）&#xA;事実&#xA;誤謬&#xA;探究&#xA;意見&#xA;節約&#xA;根拠&#xA;プロパガンダ&#xA;思慮分別（英語版）&#xA;推理&#xA;関連&#xA;修辞学&#xA;厳格&#xA;漠然（英語版）&#xA;&#xA;論理学の哲学	&#xA;構成主義&#xA;真矛盾主義&#xA;虚構主義（英語版）&#xA;有限主義（英語版）&#xA;形式主義&#xA;直観主義&#xA;論理的原子論（英語版）&#xA;論理主義&#xA;唯名論&#xA;プラトニック実在論（英語版）&#xA;プラグマティズム&#xA;実在論                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |   |
|  &#xA;メタ論理学と超数学&#xA;&#xA;&#xA;カントールの定理&#xA;決定問題&#xA;チャーチのテーゼ&#xA;無矛盾性&#xA;実効的方法（英語版）&#xA;数学基礎論&#xA;ゲーデルの完全性定理&#xA;ゲーデルの不完全性定理&#xA;健全性&#xA;完全性&#xA;決定可能性&#xA;解釈&#xA;レーヴェンハイム-スコーレムの定理&#xA;メタ定理（英語版）&#xA;充足可能性&#xA;独立性（英語版）&#xA;独立&#xA;タイプとトークンの区別&#xA;使用と言及の区別                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |   |
|  &#xA;数理論理学&#xA;&#xA;&#xA;基幹	&#xA;形式言語&#xA;構成規則&#xA;形式体系&#xA;演繹システム（英語版）&#xA;形式的証明&#xA;形式意味論&#xA;論理式&#xA;集合&#xA;元&#xA;クラス&#xA;古典論理&#xA;公理&#xA;自然演繹&#xA;推論規則&#xA;有限関係（英語版）&#xA;定理&#xA;論理的帰結&#xA;公理系&#xA;型理論&#xA;記号&#xA;統語論（英語版）&#xA;理論（英語版）&#xA;&#xA;名辞論理学（英語版）	&#xA;命題&#xA;推論&#xA;論証&#xA;妥当性&#xA;三段論法&#xA;反対の正方形&#xA;ベン図&#xA;&#xA;命題論理とブール論理	&#xA;ブール関数&#xA;命題論理&#xA;論理演算&#xA;真理値表&#xA;原子論理式&#xA;リテラル&#xA;&#xA;述語論理	&#xA;量化&#xA;全称記号&#xA;存在記号&#xA;一階述語論理&#xA;二階述語論理&#xA;高階述語論理&#xA;単項述語計算（英語版）&#xA;&#xA;標準形	&#xA;連言標準形&#xA;選言標準形&#xA;否定標準形&#xA;冠頭標準形&#xA;スコーレム標準形&#xA;節標準形&#xA;&#xA;集合論	&#xA;集合&#xA;空集合&#xA;数え上げ&#xA;外延&#xA;有限集合&#xA;関数&#xA;部分集合&#xA;冪集合&#xA;可算集合&#xA;帰納的集合&#xA;定義域&#xA;値域&#xA;順序対&#xA;非可算集合&#xA;&#xA;モデル理論	&#xA;モデル（英語版）&#xA;解釈（英語版）&#xA;超準モデル&#xA;有限モデル理論&#xA;真理値&#xA;妥当性&#xA;&#xA;証明論	&#xA;形式的証明&#xA;演繹システム（英語版）&#xA;形式体系&#xA;定理&#xA;論理的帰結&#xA;推論規則&#xA;統語論（英語版）&#xA;&#xA;再帰理論	&#xA;再帰&#xA;帰納的集合&#xA;帰納的可算集合&#xA;決定問題&#xA;チャーチ＝チューリングのテーゼ&#xA;計算可能関数&#xA;原始再帰関数&#xA;&#xA;表現	&#xA;真理値表&#xA;クワイン・マクラスキー法&#xA;カルノー図&#xA;存在グラフ&#xA;概念地図&#xA;オイラー図&#xA;ベン図&#xA;スパイダー図&#xA;タブローの方法&#xA;Xバー理論&#xA;構文木&#xA;構文解析 |   |
|  &#xA;非古典論理&#xA;&#xA;&#xA;様相論理学	&#xA;真理様相（英語版）&#xA;価値様相（英語版）&#xA;義務論理&#xA;信念様相（英語版）&#xA;認識論理&#xA;時相論理&#xA;線形時相論理&#xA;&#xA;直観主義	&#xA;直観論理&#xA;構成的解析（英語版）&#xA;ハイディング算術（英語版）&#xA;直観主義型理論&#xA;構成的集合論（英語版）&#xA;&#xA;ファジィ論理	&#xA;真理の程度（英語版）&#xA;ファジィルール（英語版）&#xA;ファジィ集合&#xA;ファジィ有限要素（英語版）&#xA;ファジィ集合演算（英語版）&#xA;&#xA;部分構造論理	&#xA;構造規則（英語版）&#xA;適切さの論理&#xA;線形論理&#xA;&#xA;矛盾許容論理	&#xA;真矛盾主義&#xA;&#xA;様相記述論理（英語版）	&#xA;存在論&#xA;オントロジー言語（英語版）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |   |
|  &#xA;論理学者&#xA;&#xA;&#xA;アンダーソン&#xA;アリストテレス&#xA;イブン・ルシュド&#xA;イブン・スィーナー&#xA;ベイン（英語版）&#xA;バーワイズ（英語版）&#xA;ベルナイス&#xA;ブール&#xA;ブーロス（英語版）&#xA;カントール&#xA;カルナップ&#xA;チャーチ&#xA;クリュシッポス&#xA;カリー&#xA;ド・モルガン&#xA;フレーゲ&#xA;ギーチ&#xA;ゲンツェン&#xA;ゲーデル&#xA;ヒルベルト&#xA;クリーネ&#xA;クリプキ&#xA;ライプニッツ&#xA;レーヴェンハイム（英語版）&#xA;ペアノ&#xA;パース&#xA;パトナム&#xA;クワイン&#xA;ラッセル&#xA;シュレーダー（英語版）&#xA;スコトゥス&#xA;スコーレム&#xA;スマリヤン&#xA;タルスキ&#xA;チューリング&#xA;ホワイトヘッド&#xA;オッカムのウィリアム&#xA;ウィトゲンシュタイン&#xA;ツェルメロ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |   |
| [![カテゴリ](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Folder_Hexagonal_Icon.svg/16px-Folder_Hexagonal_Icon.svg.png)](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Folder_Hexagonal_Icon.svg "カテゴリ")[カテゴリ](https://ja.wikipedia.org/wiki/Category:%E8%AB%96%E7%90%86%E5%AD%A6 "Category:論理学")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |   |

| [典拠管理データベース](https://ja.wikipedia.org/wiki/Help:%E5%85%B8%E6%8B%A0%E7%AE%A1%E7%90%86 "Help:典拠管理"): 国立図書館 [![ウィキデータを編集](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/10px-OOjs_UI_icon_edit-ltr-progressive.svg.png)](https://www.wikidata.org/wiki/Q192161#identifiers "ウィキデータを編集") | - [フランス](https://catalogue.bnf.fr/ark:/12148/cb11967270h)
- [BnF data](https://data.bnf.fr/ark:/12148/cb11967270h)
- [ドイツ](https://d-nb.info/gnd/4017848-1)
- [イスラエル](http://olduli.nli.org.il/F/?func=find-b\&local_base=NLX10\&find_code=UID\&request=987007545721205171)
- [アメリカ](https://id.loc.gov/authorities/sh85050802)
- [日本](https://id.ndl.go.jp/auth/ndlna/00576869)
- [チェコ](https://aleph.nkp.cz/F/?func=find-c\&local_base=aut\&ccl_term=ica=ph208851\&CON_LNG=ENG) |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

<!-- 
NewPP limit report
Parsed by mw‐web.eqiad.main‐66cc88c876‐2vpdq
Cached time: 20250115102341
Cache expiry: 2592000
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.372 seconds
Real time usage: 0.607 seconds
Preprocessor visited node count: 3379/1000000
Post‐expand include size: 181284/2097152 bytes
Template argument size: 3606/2097152 bytes
Highest expansion depth: 24/100
Expensive parser function count: 50/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 8171/5000000 bytes
Lua time usage: 0.116/10.000 seconds
Lua memory usage: 2893995/52428800 bytes
Number of Wikibase entities loaded: 1/400
-->

<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  402.237      1 -total
 26.13%  105.091      1 Template:Logic
 25.25%  101.550      1 Template:Navbox_with_collapsible_groups
 24.90%  100.142      1 Template:Reflist
 17.45%   70.209      1 Template:Cite_book
 17.36%   69.844     45 Template:仮リンク
 16.25%   65.361      1 Template:Citation/core
 14.26%   57.342      1 Template:独自研究
 12.31%   49.513      1 Template:Citation/identifier
 11.77%   47.358      1 Template:ISBN2
-->

<!-- Saved in parser cache with key jawiki:pcache:64:|#|:idhash:canonical and timestamp 20250115102341 and revision id 102059240. Rendering was triggered because: page-view
 -->
