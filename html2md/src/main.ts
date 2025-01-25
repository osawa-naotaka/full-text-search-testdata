import { unified } from 'unified'
import rehypeParse from 'rehype-parse'
import rehypeRemark from 'rehype-remark'
import remarkStringify from 'remark-stringify'
import remarkParse from 'remark-parse'
import stripMarkdown from 'strip-markdown'
import remarkGfm from 'remark-gfm'
import type { Options } from 'remark-stringify'

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

const html = `
<h1>タイトル</h1>
<p>これは<strong>太字</strong>のテキストです。</p>
<ul>
  <li>リスト1</li>
  <li>リスト2</li>
</ul>
`

const markdown = await html2md(html)
console.log(markdown)

// Markdownをプレーンテキストに変換するテスト
const plainText = await md2plain(markdown)
console.log('Plain text:')
console.log(plainText)
