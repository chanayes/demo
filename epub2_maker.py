from ebooklib import epub


def create_epub2_book(output_path):
    # 创建 EpubBook 对象
    book = epub.EpubBook()  # 明确指定版本为 2.0

    # 设置元数据
    book.set_identifier('id123456')
    book.set_title('My Sample Book')
    book.set_language('en')
    book.add_author('John Doe')

    # 加载或创建 HTML 内容
    with open('chapter1.html', 'r', encoding='utf-8') as f:
        c1_content = f.read()

    # 创建章节
    c1 = epub.EpubHtml(title='Chapter 1', file_name='chap_01.html', lang='en')
    c1.content = c1_content

    # 添加章节到书本
    book.add_item(c1)

    # 添加封面（EPUB 2.0 中封面通常是单独的 XHTML 文件而非图像项）
    cover_xhtml = epub.EpubHtml(title='Cover', file_name='cover.html', lang='en')
    cover_xhtml.content = f'<img src="cover.jpg" alt="Cover Image"/>'
    book.add_item(cover_xhtml)

    # 设置封面项
    book.set_metadata('cover', cover_xhtml.href)

    # 定义目录（TOC）
    book.toc = [epub.Link(c1.file_name, c1.title, c1.lang)]

    # 添加 NCX 导航文件（EPUB 2.0 不使用 EPUB Nav）
    book.add_item(epub.EpubNcx())

    # 设置书脊（Spine），定义阅读顺序
    book.spine = ['toc.ncx', c1]

    # 写入EPUB文件
    epub.write_epub(output_path, book, {})

    print('done')


# 使用上述函数创建EPUB 2电子书
create_epub2_book('my_sample_book.epub')
