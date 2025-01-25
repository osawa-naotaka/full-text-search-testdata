# 形式言語

**形式言語**（けいしきげんご、[Template:Lang-en-short](https://ja.wikipedia.org/wiki/Template:Lang-en-short?action=edit\&redlink=1 "Template:Lang-en-short")）とは、[文法](https://ja.wikipedia.org/wiki/%E6%96%87%E6%B3%95?action=edit\&redlink=1 "文法")や[構文](https://ja.wikipedia.org/wiki/%E6%A7%8B%E6%96%87?action=edit\&redlink=1 "構文"), [統語論](https://ja.wikipedia.org/wiki/%E7%B5%B1%E8%AA%9E%E8%AB%96?action=edit\&redlink=1 "統語論")などが、すべて形式的に与えられている[言語](https://ja.wikipedia.org/wiki/%E8%A8%80%E8%AA%9E?action=edit\&redlink=1 "言語")である。[人工言語](https://ja.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E8%A8%80%E8%AA%9E?action=edit\&redlink=1 "人工言語")の一種

[\[1\]](https://ja.wikipedia.org/wiki/#cite_note-1)

1. **[^](https://ja.wikipedia.org/wiki/#cite_ref-1)** [言語学　その1\~当たり前過ぎて意識しなくなっていること](https://note.com/lincoln246/n/nc4002055d7b8)

。

形式的でないために、しばしば曖昧さが残されたり、話者集団によって用法がうつろいていったりする[自然言語](https://ja.wikipedia.org/wiki/%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E?action=edit\&redlink=1 "自然言語")に対して、形式言語は、用法の変化に関しては非常に厳格である。

この記事では、形式的な統語論すなわち構文の形式的な定義と[形式文法](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%96%87%E6%B3%95?action=edit\&redlink=1 "形式文法")について述べる。形式的な意味論については[形式意味論](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%84%8F%E5%91%B3%E8%AB%96?action=edit\&redlink=1 "形式意味論")の記事を参照。

## 定義

形式言語の理論、特に[オートマトン理論](https://ja.wikipedia.org/wiki/%E3%82%AA%E3%83%BC%E3%83%88%E3%83%9E%E3%83%88%E3%83%B3?action=edit\&redlink=1 "オートマトン")と関連したそれにおいては、言語は[アルファベット](https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%99%E3%83%83%E3%83%88_\(%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%A6\)?action=edit\&redlink=1 "アルファベット (計算機科学)")の列（語 word） の集合である

[\[1\]](https://ja.wikipedia.org/wiki/#cite_note-1)

1. **[^](https://ja.wikipedia.org/wiki/#cite_ref-1)** Micael Sipser (2005). *Introduction to the Theory of Computation*. [ISBN](https://ja.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0534950973](https://ja.wikipedia.org/wiki/Special:BookSources/0534950973 "Special:BookSources/0534950973").

。

![{\displaystyle L\subset \Sigma ^{\*}=\\{\langle \sigma \_{1},\sigma \_{2},...\rangle |\sigma \_{i}\in \Sigma \\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/853d261f9aca42397cb084eec55c98a08c32ff90)

ただし、長さゼロの**空単語**（*Empty Word*, 記号 ![{\displaystyle e}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cd253103f0876afc68ebead27a5aa9867d927467)、![{\displaystyle \epsilon }](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3837cad72483d97bcdde49c85d3b7b859fb3fd2)、![{\displaystyle \Lambda }](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ac0a4a98a414e3480335f9ba652d12571ec6733)）も含む。 チューリングマシンの言語は単なる文字列なので、数学的構造(他のチューリングマシンを含む)を扱うには符号化([エンコード](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%89?action=edit\&redlink=1 "エンコード"))し、その数値を解釈するプログラムを埋め込む必要がある。 チューリング完全機械は十分強力なので、この手法であらゆる列挙可能な構造を扱うことができる。チューリングマシンの数値表現については(チューリングマシンの)表記(description)という。

あるチューリングマシンが存在して、言語に属するすべての語 *w* に対して動作させると受理状態で停止し、属さない語には受理しないようなとき、その言語は**チューリング認識可能**という。 また、言語に属さないときは必ず拒否状態で停止する場合、その言語は**チューリング判別可能**であるという。(この2つの違いは、一部の入力に対してチューリングマシンが停止しない場合があるかどうかである) また、チューリングマシン**TM**の言語 *L*(**TM**) とは、テープに *w* をセットしたあと、**TM**を動作させると受理状態に入って停止するような *w* の集合からなる言語(**TM**認識可能な言語)のことである。

この言語には以下のような演算が定義される。ここで、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) と ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) は共通のアルファベットから構成される言語であるとする。

- 「連結」![{\displaystyle L\_{1}L\_{2}\quad }](https://wikimedia.org/api/rest_v1/media/math/render/svg/672373692b198bda74d390ac471b75ad90ad11e6) は、文字列群 ![{\displaystyle vw}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8354a09980e3eb2de1a7d376cc69b544c43cced) から構成される。ここで、![{\displaystyle v}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e07b00e7fc0847fbd16391c778d65bc25c452597) は ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれる文字列で、![{\displaystyle w}](https://wikimedia.org/api/rest_v1/media/math/render/svg/88b1e0c8e1be5ebe69d18a8010676fa42d7961e6) は ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) に含まれる文字列である。
- 「積集合」![{\displaystyle L\_{1}\cap L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/159185961cf4ee1f5bcd827ae7efa311b81da905) は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) にも ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) にも含まれる文字列の集合である。
- 「和集合」![{\displaystyle L\_{1}\cup L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1f3ba91b5655b26d6dd518a902ac0aed95c1aca4) は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) か ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) に含まれる文字列の集合である。
- ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) の「補集合」は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれない全ての文字列の集合である。
- 「商集合」![{\displaystyle L\_{1}/L\_{2}\quad }](https://wikimedia.org/api/rest_v1/media/math/render/svg/b1cb6d6091babf386b828ec5c2c382968f861094) は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれる文字列 ![{\displaystyle vw}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8354a09980e3eb2de1a7d376cc69b544c43cced) に対して、![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) に含まれる文字列 ![{\displaystyle w}](https://wikimedia.org/api/rest_v1/media/math/render/svg/88b1e0c8e1be5ebe69d18a8010676fa42d7961e6) が存在するときに、全ての ![{\displaystyle v}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e07b00e7fc0847fbd16391c778d65bc25c452597) に相当する文字列群から構成される。
- 「[クリーネスター](https://ja.wikipedia.org/wiki/%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%8D%E3%82%B9%E3%82%BF%E3%83%BC?action=edit\&redlink=1 "クリーネスター")」![{\displaystyle L\_{1}^{\*}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cae4218ec52d028f64543a0cefae5d48fdc526f0) は、![{\displaystyle w\_{1}w\_{2}...w\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/958f88f26bdb5017d239cc3153d9a31e21f05404) という形式の全文字列群から構成される。ただし、![{\displaystyle w\_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fe22f0329d3ecb2e1880d44d191aba0e5475db68) は ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれ、![{\displaystyle n\geq 0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ce8a1b7b3bc3c790054d93629fc3b08cd1da1fd0) である。注意すべきは、![{\displaystyle n=0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/26819344e55f5e671c76c07c18eb4291fcec85ae) の場合もあるので、空文字列 ![{\displaystyle \epsilon }](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3837cad72483d97bcdde49c85d3b7b859fb3fd2) も含まれるという点である。
- 「反転」![{\displaystyle L\_{1}^{R}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6166246702d7ddfc7706cd4d7db49cbe62b3da21) は、![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) の全文字列を反転させた文字列群から構成される。
- ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) と ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) の「シャッフル」とは、![{\displaystyle v\_{1}w\_{1}v\_{2}w\_{2}...v\_{n}w\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a6eb1abcd6c2ed7aec9a0cd932948056323b7319) で表される全文字列から構成される。ここで、![{\displaystyle n\geq 1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d8ce9ce38d06f6bf5a3fe063118c09c2b6202bfe) で、![{\displaystyle v\_{1},...,v\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ed315d96db6db7b0f8d128d1347e287935132df) を連結した ![{\displaystyle v\_{1}...v\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/44f8a5511a593e6302bd8ef1cfcbea378a567852) は ![{\displaystyle L\_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0e79dc1b001f8b923df475ed14de023cbc456013) に含まれる文字列であり、![{\displaystyle w\_{1},...,w\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0b0d3622440fea8f79d0fbe7f49d9c8ac3953142) を連結した ![{\displaystyle w\_{1}...w\_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e3990ba22d8e23e3ff1d36874469c17dbb1a2fd0) は ![{\displaystyle L\_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c6a952cfe42c86b7741f55a817da0e251793a358) に含まれる文字列である。

[モデル理論](https://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%87%E3%83%AB%E7%90%86%E8%AB%96?action=edit\&redlink=1 "モデル理論")においては、言語は定数記号<!-- TMにおける2進表現文字列に相当 -->、関数記号<!-- 変換TMの文字列表現に相当 -->、述語記号<!-- 判別TMの文字列表現に相当 -->の集合である

[\[1\]](https://ja.wikipedia.org/wiki/#cite_note-1)

1. **[^](https://ja.wikipedia.org/wiki/#cite_ref-1)** 坪井明人 (2011). ["数学基礎論サマースクール モデル理論入門"](http://www2.kobe-u.ac.jp/~kikyo/LogicSummerSchool2011/lectures/2011kobe_tsuboi.pdf) (PDF). Retrieved 2012-02-18. `{{cite web}}`: Text "和書" ignored ([help](https://ja.wikipedia.org/wiki/Help:CS1_errors#text_ignored "Help:CS1 errors"))

。

![{\displaystyle L=\\{c\_{0},c\_{1},...\\}\cup \\{f\_{0},f\_{1},...\\}\cup \\{p\_{0},p\_{1},...\\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/58fcb420669fabe7e0b41015b573d2e85e63d67b)

<!--

これらの記号に意味を与える構造は、言語の対象外である。{{要出典範囲|つまり何らかの実際的な問題を言語の認識問題として定式化するには、その問題に共通する制約を構造として定義しておく必要がある。そしてそれらの定数や関数、述語を充足する問題を言語の認識問題とすることができる。}} ちょっと自信が無い -->

<!--「言語の対象外」というのも多分英語版執筆者(？)の独断？　形式言語にだって意味論はあるというか-->

## 形式文法

Main article: [形式文法](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%96%87%E6%B3%95?action=edit\&redlink=1 "形式文法")

形式言語は、[形式文法](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%96%87%E6%B3%95?action=edit\&redlink=1 "形式文法")と密接な関係がある。例として、次のような[文脈自由文法](https://ja.wikipedia.org/wiki/%E6%96%87%E8%84%88%E8%87%AA%E7%94%B1%E6%96%87%E6%B3%95?action=edit\&redlink=1 "文脈自由文法")の構文規則があるとき、

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

また、形式文法が階層をなすという[チョムスキー階層](https://ja.wikipedia.org/wiki/%E3%83%81%E3%83%A7%E3%83%A0%E3%82%B9%E3%82%AD%E3%83%BC%E9%9A%8E%E5%B1%A4?action=edit\&redlink=1 "チョムスキー階層")は、生成する言語では言語の認識に必要な最小のオートマトンが階層をなすという形で現れる。

## その他

[Template:独自研究](https://ja.wikipedia.org/wiki/Template:%E7%8B%AC%E8%87%AA%E7%A0%94%E7%A9%B6?action=edit\&redlink=1 "Template:独自研究")

### 言及される分野

形式言語は、「人や[計算機](https://ja.wikipedia.org/wiki/%E8%A8%88%E7%AE%97%E6%A9%9F?action=edit\&redlink=1 "計算機")の如何なる記号変換能力から如何なる[思考](https://ja.wikipedia.org/wiki/%E6%80%9D%E8%80%83?action=edit\&redlink=1 "思考")能力や[計算](https://ja.wikipedia.org/wiki/%E8%A8%88%E7%AE%97?action=edit\&redlink=1 "計算")能力が生まれるか」の学としての広義の[数理論理学](https://ja.wikipedia.org/wiki/%E6%95%B0%E7%90%86%E8%AB%96%E7%90%86%E5%AD%A6?action=edit\&redlink=1 "数理論理学")の研究対象であり、従って形式言語は、[哲学](https://ja.wikipedia.org/wiki/%E5%93%B2%E5%AD%A6?action=edit\&redlink=1 "哲学")・[言語学](https://ja.wikipedia.org/wiki/%E8%A8%80%E8%AA%9E%E5%AD%A6?action=edit\&redlink=1 "言語学")・[計算機科学](https://ja.wikipedia.org/wiki/%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%A6?action=edit\&redlink=1 "計算機科学")・[数学基礎論](https://ja.wikipedia.org/wiki/%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A4%8E%E8%AB%96?action=edit\&redlink=1 "数学基礎論")・[数理心理学](https://ja.wikipedia.org/wiki/%E6%95%B0%E7%90%86%E5%BF%83%E7%90%86%E5%AD%A6?action=edit\&redlink=1 "数理心理学")等々において重要な役割を演ずる。 それらの学問分野では、如何なる形式言語を研究すべきかの[文法論](https://ja.wikipedia.org/wiki/%E6%96%87%E6%B3%95?action=edit\&redlink=1 "文法")（構文論・統辞論）や形式言語の[意味論](https://ja.wikipedia.org/wiki/%E6%84%8F%E5%91%B3%E8%AB%96_\(%E6%9B%96%E6%98%A7%E3%81%95%E5%9B%9E%E9%81%BF\)?action=edit\&redlink=1 "意味論 (曖昧さ回避)")や[演繹論](https://ja.wikipedia.org/wiki/%E6%BC%94%E7%B9%B9?action=edit\&redlink=1 "演繹")が研究される。

[形式手法](https://ja.wikipedia.org/wiki/%E5%BD%A2%E5%BC%8F%E6%89%8B%E6%B3%95?action=edit\&redlink=1 "形式手法")という場合には、形式言語に加えて、模擬試験、検証・証明などの仕組みを込みで言う場合が有る。

### 自然言語への応用

Further information: [生成文法](https://ja.wikipedia.org/wiki/%E7%94%9F%E6%88%90%E6%96%87%E6%B3%95?action=edit\&redlink=1 "生成文法") and [句構造文法](https://ja.wikipedia.org/wiki/%E5%8F%A5%E6%A7%8B%E9%80%A0%E6%96%87%E6%B3%95?action=edit\&redlink=1 "句構造文法")

[自然言語](https://ja.wikipedia.org/wiki/%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E?action=edit\&redlink=1 "自然言語")を比較的単純な形式言語のモデルにあてはめて分析する言語学は、[チョムスキー](https://ja.wikipedia.org/wiki/%E3%83%8E%E3%83%BC%E3%83%A0%E3%83%BB%E3%83%81%E3%83%A7%E3%83%A0%E3%82%B9%E3%82%AD%E3%83%BC?action=edit\&redlink=1 "ノーム・チョムスキー")によって提唱された。[音素](https://ja.wikipedia.org/wiki/%E9%9F%B3%E7%B4%A0?action=edit\&redlink=1 "音素")や[語幹](https://ja.wikipedia.org/wiki/%E8%AA%9E%E5%B9%B9?action=edit\&redlink=1 "語幹")などを素記号として考える。 実際の自然言語の[構文規則](https://ja.wikipedia.org/wiki/%E6%A7%8B%E6%96%87%E8%A6%8F%E5%89%87?action=edit\&redlink=1 "構文規則")（あるいは[文法](https://ja.wikipedia.org/wiki/%E6%96%87%E6%B3%95?action=edit\&redlink=1 "文法")）は、文字通り自然発生的のものであり、形式言語における構文規則のように明確に規定するのは難しい。

ただ、素朴な文法論の主張は、形式言語の理論とみなすことができる。 素朴な文法論は、例えば次のようなものである。

- [品詞](https://ja.wikipedia.org/wiki/%E5%93%81%E8%A9%9E?action=edit\&redlink=1 "品詞")にはこのようなのものがある。
- この語はあの品詞に属す。
- この品詞に属す語をこの[活用](https://ja.wikipedia.org/wiki/%E6%B4%BB%E7%94%A8?action=edit\&redlink=1 "活用")と[組み合わせ](https://ja.wikipedia.org/wiki/%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B?action=edit\&redlink=1 "組み合わせ")と[順序](https://ja.wikipedia.org/wiki/%E9%A0%86%E5%BA%8F?action=edit\&redlink=1 "順序")とで並べると文（や[句](https://ja.wikipedia.org/wiki/%E5%8F%A5?action=edit\&redlink=1 "句")や[節](https://ja.wikipedia.org/wiki/%E7%AF%80_\(%E6%96%87%E6%B3%95\)?action=edit\&redlink=1 "節 (文法)")）になる。

こういう文法論はすなわち、素記号とは何かを定め、それらから文を作る構文規則を定めるのだから、まさに形式言語の理論である。

こういう形式言語論的な文法論は、実際の言語と比較することで自然言語の特徴を浮き彫りにし、自然言語のより深い理解へと導くことを可能とすることもなくはない。言語そのものではなく、言語行動の深層をなす人間精神を探るためには、むしろこういう文法論を数学化し、更に[意味論](https://ja.wikipedia.org/wiki/%E6%84%8F%E5%91%B3%E8%AB%96_\(%E6%9B%96%E6%98%A7%E3%81%95%E5%9B%9E%E9%81%BF\)?action=edit\&redlink=1 "意味論 (曖昧さ回避)")・文法論を伴った論理学にまで推し進めることが有意義ともいえよう。

## 脚注

[Template:脚注ヘルプ](https://ja.wikipedia.org/wiki/Template:%E8%84%9A%E6%B3%A8%E3%83%98%E3%83%AB%E3%83%97?action=edit\&redlink=1 "Template:脚注ヘルプ")

[![](https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png)](https://ja.wikipedia.org/wiki/File:Commons-logo.svg)

Wikimedia Commons has media related to [Formal languages](https://commons.wikimedia.org/wiki/Category:Formal%20languages "commons:Category:Formal languages").

**Preview warning:** Commons category does not match the Commons sitelink on Wikidata – [please check](https://ja.wikipedia.org/wiki/Template:Commons_category#Resolving_discrepancies "Template:Commons category")

| - [v](https://ja.wikipedia.org/wiki/Template:Logic "Template:Logic")
- [t](https://ja.wikipedia.org/wiki/Template_talk:Logic "Template talk:Logic")
- [e](https://ja.wikipedia.org/wiki/Special:EditPage/Template:Logic "Special:EditPage/Template:Logic")[Logic](https://ja.wikipedia.org/wiki/Logic "Logic")                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| * [Outline](https://ja.wikipedia.org/wiki/Outline_of_logic "Outline of logic")
* [History](https://ja.wikipedia.org/wiki/History_of_logic "History of logic")                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Major fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | - [Computer science](https://ja.wikipedia.org/wiki/Logic_in_computer_science "Logic in computer science")
- [Formal semantics (natural language)](https://ja.wikipedia.org/wiki/Formal_semantics_\(natural_language\) "Formal semantics (natural language)")
- [Inference](https://ja.wikipedia.org/wiki/Inference "Inference")
- [Philosophy of logic](https://ja.wikipedia.org/wiki/Philosophy_of_logic "Philosophy of logic")
- [Proof](https://ja.wikipedia.org/wiki/Formal_proof "Formal proof")
- [Semantics of logic](https://ja.wikipedia.org/wiki/Semantics_of_logic "Semantics of logic")
- [Syntax](https://ja.wikipedia.org/wiki/Syntax_\(logic\) "Syntax (logic)")Logics&#xA;Classical&#xA;Informal&#xA;Critical thinking&#xA;Reason&#xA;Mathematical&#xA;Non-classical&#xA;Philosophical&#xA;&#xA;Theories	&#xA;Argumentation&#xA;Metalogic&#xA;Metamathematics&#xA;Set                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Foundations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | * [Abduction](https://ja.wikipedia.org/wiki/Abductive_reasoning "Abductive reasoning")

* [Analytic and synthetic propositions](https://ja.wikipedia.org/wiki/Analytic%E2%80%93synthetic_distinction "Analytic–synthetic distinction")

* [Antecedent](https://ja.wikipedia.org/wiki/Antecedent_\(logic\) "Antecedent (logic)")

* [Consequent](https://ja.wikipedia.org/wiki/Consequent "Consequent")

* [Contradiction](https://ja.wikipedia.org/wiki/Contradiction "Contradiction")

  - [Paradox](https://ja.wikipedia.org/wiki/Paradox "Paradox")
  - [Antinomy](https://ja.wikipedia.org/wiki/Antinomy "Antinomy")

* [Deduction](https://ja.wikipedia.org/wiki/Deductive_reasoning "Deductive reasoning")

* [Deductive closure](https://ja.wikipedia.org/wiki/Deductive_closure "Deductive closure")

* [Definition](https://ja.wikipedia.org/wiki/Definition "Definition")

* [Description](https://ja.wikipedia.org/wiki/Description "Description")

* [Entailment](https://ja.wikipedia.org/wiki/Logical_consequence "Logical consequence")
  - [Linguistic](https://ja.wikipedia.org/wiki/Entailment_\(linguistics\) "Entailment (linguistics)")

* [Form](https://ja.wikipedia.org/wiki/Logical_form "Logical form")

* [Induction](https://ja.wikipedia.org/wiki/Inductive_reasoning "Inductive reasoning")

* [Logical truth](https://ja.wikipedia.org/wiki/Logical_truth "Logical truth")

* [Name](https://ja.wikipedia.org/wiki/Name "Name")

* [Necessity and sufficiency](https://ja.wikipedia.org/wiki/Necessity_and_sufficiency "Necessity and sufficiency")

* [Premise](https://ja.wikipedia.org/wiki/Premise "Premise")

* [Probability](https://ja.wikipedia.org/wiki/Probability "Probability")

* [Proposition](https://ja.wikipedia.org/wiki/Proposition "Proposition")

* [Reference](https://ja.wikipedia.org/wiki/Reference "Reference")

* [Statement](https://ja.wikipedia.org/wiki/Statement_\(logic\) "Statement (logic)")

* [Substitution](https://ja.wikipedia.org/wiki/Substitution_\(logic\) "Substitution (logic)")

* [Truth](https://ja.wikipedia.org/wiki/Truth "Truth")

* [Validity](https://ja.wikipedia.org/wiki/Validity_\(logic\) "Validity (logic)") |
| Lists                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | topics&#xA;Mathematical logic&#xA;Boolean algebra&#xA;Set theory&#xA;&#xA;other	&#xA;Logicians&#xA;Rules of inference&#xA;Paradoxes&#xA;Fallacies&#xA;Logic symbols                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - ![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Socrates.png/18px-Socrates.png) [Philosophy portal](https://ja.wikipedia.org/wiki/Portal:Philosophy "Portal:Philosophy")
- [Category](https://ja.wikipedia.org/wiki/Category:Logic "Category:Logic")
- [WikiProject](https://ja.wikipedia.org/wiki/Wikipedia:WikiProject_Logic "Wikipedia:WikiProject Logic") ([talk](https://ja.wikipedia.org/wiki/Wikipedia_talk:WikiProject_Logic "Wikipedia talk:WikiProject Logic"))
- [changes](https://en.wikipedia.org/w/index.php?title=Special:Recentchangeslinked\&target=Template:Logic\&hidebots=0) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
