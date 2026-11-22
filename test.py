# 1. search(): tìm bản ghi theo điều kiện (domain)
cues = self.env['product.template'].search(
    [('categ_id.name', '=', 'Cơ & Ngọn cơ'), ('list_price', '>', 5000000)],
    limit=10
)

# 2. browse(): lấy bản ghi theo id
product = self.env['product.template'].browse(15)
print(product.name)

# 3. create(): tạo mới bản ghi
new_partner = self.env['res.partner'].create({
    'name': 'Quán Bida Sao Mai',
    'phone': '0901234567',
    'customer_rank': 1,
})

# 4. write(): cập nhật bản ghi
new_partner.write({'phone': '0987654321'})

# 5. unlink(): xóa bản ghi
new_partner.unlink()
