var now_url = window.location.href
var url_list = now_url.split('/')
var order_id = url_list[url_list.length-2]
var api_url = "http://120.24.4.254:5455/api/order/"+order_id+"/?page=1&num=100"

var back = document.getElementById("back")
back.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/order/"
})

fetch(api_url).then(function(res){
	if(res.ok){
	console.log("success")
		return res.json()
 	}
	else
		console.log("error")
}).then(res => {
	var i;
	detail=res.detail
	var body=document.getElementById("body")
	var old_div=body.getElementsByTagName("div")
	for(od=0;old_div.length!=0;){
		body.removeChild(old_div[od])
	}
	for(i=0;i<detail.length;i++){
		var div=document.createElement("div")
		div.setAttribute("id","detail"+i) 
		div.setAttribute("class","detail")
		var body=document.getElementById("body")
		body.appendChild(div)

		var count=document.createElement("p")
		count.setAttribute("id","count") 
		var count_node=document.createTextNode("数量："+detail[i].count)
		count.appendChild(count_node)
		div.appendChild(count)

		var cost=document.createElement("p")
		cost.setAttribute("id","cost") 
		var cost_node=document.createTextNode("总额："+detail[i].cost)
		cost.appendChild(cost_node)
		div.appendChild(cost)

		var bookname=document.createElement("p")
		bookname.setAttribute("id","bookname") 
		var bookname_node=document.createTextNode("书本名称："+detail[i].bookname)
		bookname.appendChild(bookname_node)
		div.appendChild(bookname)

		var image_url=document.createElement("p")
		image_url.setAttribute("id","image_url") 
		var image_url_node=document.createTextNode("图片："+detail[i].image_url)
		image_url.appendChild(image_url_node)
		div.appendChild(image_url)

		var selling_price=document.createElement("p")
		selling_price.setAttribute("id","selling_price") 
		var selling_price_node=document.createTextNode("单价："+detail[i].selling_price)
		selling_price.appendChild(selling_price_node)
		div.appendChild(selling_price)
	}
})	