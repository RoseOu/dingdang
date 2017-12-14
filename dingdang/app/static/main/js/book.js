var now_url = window.location.href
var url_list = now_url.split('/')
var book_id = url_list[url_list.length-2]
var api_url = "http://120.24.4.254:5455/api/book/"+book_id+"/"

var register = document.getElementById("register")
var login = document.getElementById("login")
var back = document.getElementById("back")
var cart = document.getElementById("cart")

register.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/register/"
})
login.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/login/"
})
back.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/home/"
})


var count = document.getElementById('count');
//var id = cookie.getCookie('id');
var user_id = 2; //chrome关闭跨域时使用
cart.addEventListener('click', function(){
	    fetch("http://120.24.4.254:5455/api/cart/add/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_id: user_id,
            book_id: book_id,
            count: count.value
        })
    }).then(res => {
        if (res.ok)
            return res.json()
        else
            console.log("error");
    }).then(value => {
    	alert("加入购物车成功！")
    })
})

fetch(api_url).then(function(res){
	if(res.ok){
	console.log("success")
		return res.json()
 	}
	else
		console.log("error")
}).then(res => {
	book=document.getElementById("book")

	var name=document.createElement("p")
	name.setAttribute("id","name") 
	var name_node=document.createTextNode(res.name)
	name.appendChild(name_node)
	book.appendChild(name)

	var author=document.createElement("p")
	author.setAttribute("id","author") 
	var author_node=document.createTextNode(res.author)
	author.appendChild(author_node)
	book.appendChild(author)

	var translator=document.createElement("p")
	translator.setAttribute("id","translator") 
	var translator_node=document.createTextNode(res.translator)
	translator.appendChild(translator_node)
	book.appendChild(translator)

	var market_price=document.createElement("p")
	market_price.setAttribute("id","market_price") 
	var market_price_node=document.createTextNode(res.market_price)
	market_price.appendChild(market_price_node)
	book.appendChild(market_price)

	var selling_price=document.createElement("p")
	selling_price.setAttribute("id","selling_price") 
	var selling_price_node=document.createTextNode(res.selling_price)
	selling_price.appendChild(selling_price_node)
	book.appendChild(selling_price)

	var press=document.createElement("p")
	press.setAttribute("id","press") 
	var press_node=document.createTextNode(res.press)
	press.appendChild(press_node)
	book.appendChild(press)

	var edition=document.createElement("p")
	edition.setAttribute("id","edition") 
	var edition_node=document.createTextNode(res.edition)
	edition.appendChild(edition_node)
	book.appendChild(edition)

	var publication_time=document.createElement("p")
	publication_time.setAttribute("id","publication_time") 
	var publication_time_node=document.createTextNode(res.publication_time)
	publication_time.appendChild(publication_time_node)
	book.appendChild(publication_time)

	var version=document.createElement("p")
	version.setAttribute("id","version") 
	var version_node=document.createTextNode(res.version)
	version.appendChild(version_node)
	book.appendChild(version)

	var series=document.createElement("p")
	series.setAttribute("id","series") 
	var series_node=document.createTextNode(res.series)
	series.appendChild(series_node)
	book.appendChild(series)

	var language=document.createElement("p")
	language.setAttribute("id","language") 
	var language_node=document.createTextNode(res.language)
	language.appendChild(language_node)
	book.appendChild(language)

	var binding=document.createElement("p")
	binding.setAttribute("id","binding") 
	var binding_node=document.createTextNode(res.binding)
	binding.appendChild(binding_node)
	book.appendChild(binding)

	var introduction=document.createElement("p")
	introduction.setAttribute("id","introduction") 
	var introduction_node=document.createTextNode(res.introduction)
	introduction.appendChild(introduction_node)
	book.appendChild(introduction)

	var catalog=document.createElement("p")
	catalog.setAttribute("id","catalog") 
	var catalog_node=document.createTextNode(res.catalog)
	catalog.appendChild(catalog_node)
	book.appendChild(catalog)

	var inventory=document.createElement("p")
	inventory.setAttribute("id","inventory") 
	var inventory_node=document.createTextNode(res.inventory)
	inventory.appendChild(inventory_node)
	book.appendChild(inventory)

	var number=document.createElement("p")
	number.setAttribute("id","number") 
	var number_node=document.createTextNode(res.number)
	number.appendChild(number_node)
	book.appendChild(number)

	var sale=document.createElement("p")
	sale.setAttribute("id","sale") 
	var sale_node=document.createTextNode(res.sale)
	sale.appendChild(sale_node)
	book.appendChild(sale)

	var image_url=document.createElement("p")
	image_url.setAttribute("id","image_url") 
	var image_url_node=document.createTextNode(res.image_url)
	image_url.appendChild(image_url_node)
	book.appendChild(image_url)
})	

