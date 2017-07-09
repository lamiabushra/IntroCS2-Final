#! /usr/bin/python
print "content-type: text/html\n\r"

import cgi, cgitb
cgitb.enable()

fromQS = cgi.FieldStorage ()

new = str(fromQS)

amtPuppy = new.count('Puppy')
amtBunny = new.count('Bunny')
amtKitten = new.count('Kitten')
amtCockatiel = new.count('Cockatiel')

newlist = []
newlist.append(amtPuppy)
newlist.append(amtBunny)
newlist.append(amtKitten)
newlist.append(amtCockatiel)

animalnumber = max(newlist)
chanimalnumber = newlist.index(animalnumber)
chanimal = ['Puppy', 'Bunny', 'Kitten', 'Cockatiel']
animal = chanimal[chanimalnumber]

html = '''
<!DOCTYPE html>
<script language="javascript" type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>

<meta name="color:background" content="#f6f6f6"/>
<meta name="color:title" content="#eeeeee">
<meta name="color:hover" content="#cccccc">

<meta name="image:background" content=""/>
<meta name="image:header" content=""/>

<style type="text/css">
#titlee{
	width:1334px;
	height:110px;
	box-shadow:0px 2px 3px rgba(0,0,0,.15);
	top:0px;
	opacity:1;
	position:absolute;
	font-family: 'arial', sans-serif;
	letter-spacing:3px;
	font-style:none;
	text-align:center;
	font-weight:bold;
	padding:13px;
	color:#ffffff;
	text-transform:uppercase;
	line-height:45px;
	font-size:16px;
	margin-left:0px;
	background:#000000;
	z-index:9999;
}
#titlee:first-letter {
	font-size:20px;
	font-weight:bold;
	text-align:center;
	font-family: 'arial', sans-serif;
	color:#ddd;
	padding:0px;
}
#header{
	position:absolute;
	opacity:1;
	width:1000px;
	height:400px;
	top:80px;
	background:#EEEEEE;
	margin-left:180px;
	z-index:9999999;
}
#header img{
	width:1000px;
	height:400px;
}
#header {
	position:fixed;
	margin-top:190px;
	padding:10px;
	margin-left:180px;
	background-color:transparent;
	z-index:9999999999999999;
}
#headerimage {
	z-index:-99999;
}
#headerimage img {
	width:1000px;
	height:400px;
	left:180px;
	top:80px;
	position:absolute;
	background:#EEEEEE;
	z-index:99999;
}
ul {
 	list-style-type: none;	
	margin: 0;
 	padding: 0;
	position: relative;
	top: 150px;
	font-family: 'arial', sans-serif;
	font-weight: bold;
	font-size: 10px;
	width:200px;
	text-transform: uppercase;
	line-height:45px;
	font-size:16px;
	letter-spacing:3px;
	font-style:none;
	background-color:#00000;
	font-color:#fffff;
}
li a {
    display: block;
    color: #000;
    padding: 8px 16px;
    text-decoration: none;
}
.active {
    background-color: #4CAF50;
    color: white;
}
li a:hover {
    background-color: #555;
    color: white;
}
</style>

<ul>
  <li><a href="nature.html">Home</a></li>
  <li><a href="about.html">About Us!</a></li>
  <li><a href="quiz1.html">What Animal Are You?</a></li>
  <li><a href="quiz2.html">What Pet Should You Own?</a></li>

</ul> 

<body>

<div id="sidebar">
<div id="titlee">Results</div>
<div id="headerimage" ><img src="http://www.championsafaris.com/images/images/zebra.jpg"></a>

<div style="background-color:black;color:white;padding:20px;margin:auto;position:absolute;top:500px;left:180px;font-family: 'arial', sans-serif;">
<h2 style = "text=transform:uppercase;letter-spacing:2px; font-weight:bold;">And your result is:</h2>
<h1 style= "text-tranform:uppercase">ANIMAL</h1>



</body>
</html>

'''

htmll = html.replace("ANIMAL", animal)
print htmll
