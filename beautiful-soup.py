from bs4 import BeautifulSoup

html_doc = """<html><head> <title>Book Page Title</title></head><body> <h1>This is a test page</h1><div class="cont\ent" id="div1"> Python Book List - <ul> <li><a href="https://dimik.pub/book/155">Learn Programming with Python - Part 1\</a></li><li><a href="https://dimik.pub/book/181">Learn Programming with Python - Part 2</a></li> <li><a href="https://\dimik.pub/book/249">Learn Programming with Python - Part 3</a></li> </ul></div><div class="content" id="div2"> C Book L\ist - <ul><li><a href="https://dimik.pub/book/351">Computer Programming - Part 1</a></li><li><a href="https://dimik.pub\/book/97">Computer Programming - Part 2</a></li><li><a href="https://dimik.pub/book/245">Computer Programming - Part 3<\/a></li></ul> </div></body></html>"""
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.get_text())
# ' Book Page Title This is a test page Python Book List -  Learn Programming with Python - Part 1Learn Programming with Python - Part 2 Learn Programming with Python - Part 3  C Book List - Computer Programming - Part 1Computer Programming - Part 2Computer Programming - Part 3 '
print(soup.title)
# <title>Book Page Title</title>
print(soup.title.string)
# 'Book Page Title'
print(dir(soup.title))
# ['EMPTY_ELEMENT_EVENT', 'END_ELEMENT_EVENT', 'MAIN_CONTENT_STRING_TYPES', 'START_ELEMENT_EVENT', 'STRING_ELEMENT_EVENT', '_TreeTraversalEvent', '__annotations__', '__bool__', '__call__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_all_strings', '_event_stream', '_find_all', '_find_one', '_format_tag', '_indent_string', '_insert', '_is_xml', '_lastRecursiveChild', '_last_descendant', '_namespaces', '_self_and', '_should_pretty_print', 'append', 'attribute_value_list_class', 'attrs', 'can_be_empty_element', 'cdata_list_attributes', 'childGenerator', 'children', 'clear', 'contents', 'copy_self', 'css', 'decode', 'decode_contents', 'decompose', 'decomposed', 'default', 'descendants', 'encode', 'encode_contents', 'extend', 'extract', 'fetchAllPrevious', 'fetchNextSiblings', 'fetchParents', 'fetchPreviousSiblings', 'find', 'findAll', 'findAllNext', 'findAllPrevious', 'findChild', 'findChildren', 'findNext', 'findNextSibling', 'findNextSiblings', 'findParent', 'findParents', 'findPrevious', 'findPreviousSibling', 'findPreviousSiblings', 'find_all', 'find_all_next', 'find_all_previous', 'find_next', 'find_next_sibling', 'find_next_siblings', 'find_parent', 'find_parents', 'find_previous', 'find_previous_sibling', 'find_previous_siblings', 'format_string', 'formatter_for_name', 'get', 'getText', 'get_attribute_list', 'get_text', 'has_attr', 'has_key', 'hidden', 'index', 'insert', 'insert_after', 'insert_before', 'interesting_string_types', 'isSelfClosing', 'is_empty_element', 'known_xml', 'name', 'namespace', 'next', 'nextGenerator', 'nextSibling', 'nextSiblingGenerator', 'next_element', 'next_elements', 'next_sibling', 'next_siblings', 'parent', 'parentGenerator', 'parents', 'parserClass', 'parser_class', 'prefix', 'preserve_whitespace_tags', 'prettify', 'previous', 'previousGenerator', 'previousSibling', 'previousSiblingGenerator', 'previous_element', 'previous_elements', 'previous_sibling', 'previous_siblings', 'recursiveChildGenerator', 'renderContents', 'replaceWith', 'replaceWithChildren', 'replace_with', 'replace_with_children', 'select', 'select_one', 'self_and_descendants', 'self_and_next_elements', 'self_and_next_siblings', 'self_and_parents', 'self_and_previous_elements', 'self_and_previous_siblings', 'setup', 'smooth', 'sourceline', 'sourcepos', 'string', 'strings', 'stripped_strings', 'text', 'unwrap', 'wrap']

print(soup.title.parent.name)
# 'head'

print(soup.find_all("a"))
# [<a href="https://dimik.pub/book/155">Learn Programming with Python - Part 1</a>, <a href="https://dimik.pub/book/181">Learn Programming with Python - Part 2</a>, <a href="https://dimik.pub/book/249">Learn Programming with Python - Part 3</a>, <a href="https://dimik.pub/book/351">Computer Programming - Part 1</a>, <a href="https://dimik.pub/book/97">Computer Programming - Part 2</a>, <a href="https://dimik.pub/book/245">Computer Programming - Part 3</a>]

print(soup.div)
# <div class="content" id="div1"> Python Book List - <ul> <li><a href="https://dimik.pub/book/155">Learn Programming with Python - Part 1</a></li><li><a href="https://dimik.pub/book/181">Learn Programming with Python - Part 2</a></li> <li><a href="https://dimik.pub/book/249">Learn Programming with Python - Part 3</a></li> </ul></div>

print(soup.div.find_next_sibling())
# <div class="content" id="div2"> C Book List - <ul><li><a href="https://dimik.pub/book/351">Computer Programming - Part 1</a></li><li><a href="https://dimik.pub/book/97">Computer Programming - Part 2</a></li><li><a href="https://dimik.pub/book/245">Computer Programming - Part 3</a></li></ul> </div>

div = soup.div.find_next_sibling()
print(div.find_next_sibling())
# None

div = soup.dev
links = div.find_all("a")
for link in links:
    name, url = link.string, link.get("href")
    print(name, url)

# 'Learn Programming with Python - Part 1'
# 'https://dimik.pub/book/155'
# 'Learn Programming with Python - Part 2'
# 'https://dimik.pub/book/181'
# 'Learn Programming with Python - Part 3'
# 'https://dimik.pub/book/249'