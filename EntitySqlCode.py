from EntityData import text,sql_boiler_code

data = [i.split('→')[0].strip() for i in text.split('\n') if i]

ans = ""
for i in data:
    ans += sql_boiler_code.format(i)

print(ans)