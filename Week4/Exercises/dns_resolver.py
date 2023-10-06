import dns.resolver

result = dns.resolver.resolve('google.com', 'A')
for val in result:
    print('A Record: ', val.to_text())