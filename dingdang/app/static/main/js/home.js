var url_all = "http://120.24.4.254:5455/api/book/?category=0&page=1"
var url_category1 = "http://120.24.4.254:5455/api/book/?category=1&page=1"
var url_category2 = "http://120.24.4.254:5455/api/book/?category=2&page=1"
var url_category3 = "http://120.24.4.254:5455/api/book/?category=3&page=1"

var all = document.getElementById("all")
var category1 = document.getElementById("category1")
var category2 = document.getElementById("category2")
var category3 = document.getElementById("category3")

all.addEventListener("click", get_book.bind(window,url_all))
category1.addEventListener('click', get_book.bind(window,url_category1))
category2.addEventListener('click', get_book.bind(window,url_category2))
category3.addEventListener('click', get_book.bind(window,url_category3))

var register = document.getElementById("register")
var login = document.getElementById("login")
var profile = document.getElementById("profile")
var mycart = document.getElementById("mycart")
var myorder = document.getElementById("myorder")

register.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/register/"
})
login.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/login/"
})
//var id = cookie.getCookie('id');
var id=2;
profile.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/profile/"+id+"/"
})
mycart.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/mycart/"
})
myorder.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/myorder/"
})


var search_button = document.getElementById("search-button")

search_button.addEventListener("click", function(){
	var text = document.getElementById("search-text").value
	var value = document.getElementById("select-category").value
	var url_search = "http://120.24.4.254:5455/api/search/?body="+text+"&category="+value+"&page=1"
	get_book(url_search)
})


function get_book(url){
	fetch(url).then(function(res){
		if(res.ok){
		console.log("success")
			return res.json()
	 	}
		else
			console.log("error")
	}).then(res => {
		var i;
		book=res.book
		var body=document.getElementById("body")
		var old_div=body.getElementsByTagName("div")
		for(od=0;old_div.length!=0;){
			body.removeChild(old_div[od])
		}
		for(i=0;i<book.length;i++){
			var div=document.createElement("div")
			div.setAttribute("id","book"+i) 
			div.setAttribute("class","book")
			var body=document.getElementById("body")
			body.appendChild(div)

			var book_id=document.createElement("p")
			book_id.setAttribute("id","book_id") 
			var book_id_node=document.createTextNode(book[i].book_id)
			book_id.appendChild(book_id_node)
			div.appendChild(book_id)

			var name=document.createElement("a")
			name.setAttribute("id","name") 
			name.setAttribute("href","../book/"+book[i].book_id+"/") 
			var name_node=document.createTextNode(book[i].name)
			name.appendChild(name_node)
			div.appendChild(name)

			var author=document.createElement("p")
			author.setAttribute("id","author") 
			var author_node=document.createTextNode(book[i].author)
			author.appendChild(author_node)
			div.appendChild(author)

			var selling_price=document.createElement("p")
			selling_price.setAttribute("id","selling_price") 
			var selling_price_node=document.createTextNode(book[i].selling_price)
			selling_price.appendChild(selling_price_node)
			div.appendChild(selling_price)

			var introduction=document.createElement("p")
			introduction.setAttribute("id","introduction") 
			var introduction_node=document.createTextNode(book[i].introduction)
			introduction.appendChild(introduction_node)
			div.appendChild(introduction)

			var sale=document.createElement("p")
			sale.setAttribute("id","sale") 
			var sale_node=document.createTextNode(book[i].sale)
			sale.appendChild(sale_node)
			div.appendChild(sale)

			var image=document.createElement("p")
			image.setAttribute("id","image") 
			var image_node=document.createTextNode(book[i].image)
			image.appendChild(image_node)
			div.appendChild(image)
		}
	})	
}