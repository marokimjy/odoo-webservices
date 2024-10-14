import xmlrpc.client

# Odoo 서버에 연결하는 코드
url = 'http://localhost:8069'
db = 'odoo'
username = 'admin'
password = 'admin'

# common 서비스에 연결 (사용자 인증)
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

if uid:
    print(f"Authenticated as {username} (uid: {uid})")
else:
    print("Authentication failed!")

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password, 'res.partner', 'name_search', ['Department'], {'limit': 10})
models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])

ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'limit': 1})
[record] = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids])
models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})
models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
