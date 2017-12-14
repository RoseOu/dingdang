
var register = document.getElementById("register")
var login = document.getElementById("login")
var back = document.getElementById("back")

register.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/register/"
})
login.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/login/"
})
back.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/home/"
})

//var user_id = cookie.getCookie('id');
var user_id=2;

var url = "http://120.24.4.254:5455/api/cart/?page=1&num=100"

fetch(url, {
	method: 'POST',
	headers: {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json',
	},
	body: JSON.stringify({
	    user_id: user_id,
	})
}).then(res => {
	if (res.ok)
	    return res.json()
	else
	    console.log("error");
	}).then(value => {
		var i;
		cart=value.cart
		var body=document.getElementById("body")
		var old_div=body.getElementsByTagName("div")
		for(od=0;old_div.length!=0;){
			body.removeChild(old_div[od])
		}
		for(i=0;i<cart.length;i++){
			var div=document.createElement("div")
			div.setAttribute("id","cart"+i) 
			div.setAttribute("class","cart")
			var body=document.getElementById("body")
			body.appendChild(div)

			var cart_id=document.createElement("p")
			cart_id.setAttribute("id","cart_id") 
			var cart_id_node=document.createTextNode(cart[i].cart_id)
			cart_id.appendChild(cart_id_node)
			div.appendChild(cart_id)

			var name=document.createElement("p")
			name.setAttribute("id","name") 
			var name_node=document.createTextNode(cart[i].name)
			name.appendChild(name_node)
			div.appendChild(name)

			var selling_price=document.createElement("p")
			selling_price.setAttribute("id","selling_price") 
			var selling_price_node=document.createTextNode(cart[i].selling_price)
			selling_price.appendChild(selling_price_node)
			div.appendChild(selling_price)

			var count=document.createElement("p")
			count.setAttribute("id","count") 
			var count_node=document.createTextNode(cart[i].count)
			count.appendChild(count_node)
			div.appendChild(count)

			var sumup=document.createElement("p")
			sumup.setAttribute("id","sumup") 
			var sumup_node=document.createTextNode(cart[i].sumup)
			sumup.appendChild(sumup_node)
			div.appendChild(sumup)
		}	
})

