import pathlib

p = pathlib.Path('frontend/src/pages/BookDetailPage.tsx')
content = p.read_text(encoding='utf-8')

# 1. Add highlightApi to imports
content = content.replace(
    'import { bookApi, analyzeApi, type Book } from "../api"',
    'import { bookApi, analyzeApi, highlightApi, type Book } from "../api"'
)

# 2. Add deleteHighlightMutation after updateMutation
delete_mutation_block = '''  const deleteMutation = useMutation({
    mutationFn: () => bookApi.delete(id!),
    onSuccess: () => {
      message.success("删除成功")
      navigate("/books")
    },
    onError: () => {
      message.error("删除失败")
    },
  })

  const deleteHighlightMutation = useMutation({
    mutationFn: (highlightId: string) => highlightApi.delete(highlightId),
    onSuccess: () => {
      message.success("笔记已删除")
      queryClient.invalidateQueries({ queryKey: ["book", id, "highlights"] })
      queryClient.invalidateQueries({ queryKey: ["book", id] })
    },
    onError: (err: any) => {
      message.error("删除笔记失败: " + (err?.response?.data?.detail || err.message || ""))
    },
  })'''

content = content.replace(
    '''  const deleteMutation = useMutation({
    mutationFn: () => bookApi.delete(id!),
    onSuccess: () => {
      message.success("删除成功")
      navigate("/books")
    },
    onError: () => {
      message.error("删除失败")
    },
  })''',
    delete_mutation_block
)

# 3. Add handleDeleteHighlight function after handleAnalyze
handle_delete_fn = '''  const handleDeleteHighlight = (highlightId: string) => {
    Modal.confirm({
      title: "确认删除",
      content: "确定要删除这条笔记吗？此操作不可撤销。",
      okText: "确认",
      cancelText: "取消",
      okButtonProps: { danger: true },
      onOk: () => deleteHighlightMutation.mutate(highlightId),
    })
  }'''

content = content.replace(
    '''  const startEdit = () => {''',
    handle_delete_fn + '\n\n  const startEdit = () => {'
)

# 4. Add delete button on each highlight card's Space
old_space = '''              <Space wrap>
                {item.chapter && ('''
new_space = '''              <Space wrap style={{ justifyContent: "space-between", width: "100%" }}>
                <Space wrap>
                {item.chapter && ('''
content = content.replace(old_space, new_space)

# Close the inner Space and add delete button
old_close = '''                {item.url && (
                  <a href={item.url} target="_blank" rel="noopener noreferrer">
                    <LinkOutlined /> 原文链接
                  </a>
                )}
              </Space>'''
new_close = '''                {item.url && (
                  <a href={item.url} target="_blank" rel="noopener noreferrer">
                    <LinkOutlined /> 原文链接
                  </a>
                )}
                </Space>
                <Button
                  type="text"
                  danger
                  size="small"
                  icon={<DeleteOutlined />}
                  onClick={(e) => {
                    e.stopPropagation()
                    handleDeleteHighlight(item.id)
                  }}
                  style={{ color: "rgba(255,255,255,0.5)", flexShrink: 0 }}
                />
              </Space>'''
content = content.replace(old_close, new_close)

p.write_text(content, encoding='utf-8')
print('Updated BookDetailPage with highlight delete')
