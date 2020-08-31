geo = {
'israel' : 'Jerusalem'
'south afreica' : 'pretoria'
}

value = geo['south africa']

geo = {
'israel' : 'Jerusalem'
'south afreica' : ['pretoria', 'joburg', 'capetown'
}
value = geo['2']


geo = {
  'israel' : 'Jerusalem'
  'south africa' : [
    {
      'name' : 'pretoria'},
      {'name' : 'joburg'
      'industry' : ['finance', 'retail']
      },
      {'name' : 'capetown'}
      ]
      }

print(geo['south africa'][1]['industry'][1])


nums = [1,2,3,4,5,6,7]
for_squares

map(function, array)


# Series: 1/1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16

def series_sum(n):
  total = 0
  for i in range(1, n + 1):
  demoniator = 1
  total += 1/demoniator
  demoniator += 3

  return str(round(total, 2))




def series_sum(3)



def encrypt(text)
encrypted_message = ""
    for letter in text:
        encrypted_message += chr(ord(letter) + 3)
        return encrypted_message

def decrypt(cypher)
text = ""
    for letter in cypher:
        encrpyted encrypted_message += chr(ord(letter) - 3)
        return encrypted_message

def caeser(text, num):
    out_text = ""
    for letter in text:
        out_text += chr(ord(letter) + num)
    return out_text

    def decrypt(text, num = 3):
        return ceaser(text, -1*num)

    def encrypt(text, num = 3):
        return ceaser(text, num)



ord('c')
#99 + 3

char(99)



test.assert_equals(series_sum(1), '1.00')
