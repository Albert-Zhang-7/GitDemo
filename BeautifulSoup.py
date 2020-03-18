from bs4 import BeautifulSoup

myHtml = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>this is my title</title>
</head>
<body>
<h1> This is H1, boys.</h1>
<h1> This is another H1, boys.</h1>
<h2>This is H2, girls.</h2>
<p> this is albert, i love the video. </p>
</body>
</html>
'''
Mysoup = BeautifulSoup(myHtml, 'html.parser')
MyH1 = Mysoup.find('h1')
print(MyH1)
print(MyH1.string)

H1 = Mysoup.findAll('h1')
for i in H1:
    print(i.string)
