var url_all = "http://120.24.4.254:5455/api/order/?page=1&num=100"


var all = document.getElementById("all")
var status1 = document.getElementById("status1")
var status2 = document.getElementById("status2")
var status3 = document.getElementById("status3")
var status3 = document.getElementById("status5")

all.addEventListener("click", get_order.bind(window,url_all,0))
status1.addEventListener('click', get_order.bind(window,url_all,1))
status2.addEventListener('click', get_order.bind(window,url_all,2))
status3.addEventListener('click', get_order.bind(window,url_all,3))
status5.addEventListener('click', get_order.bind(window,url_all,5))

var back = document.getElementById("back")
back.addEventListener('click', function(){
	window.location = "http://120.24.4.254:5455/main/home/"
})

//var user_id = cookie.getCookie('id');
var user_id=2;

function get_order(url,status){
	fetch(url, {
		method: 'POST',
		headers: {
		    'Accept': 'application/json',
		    'Content-Type': 'application/json',
		},
		body: JSON.stringify({
		    user_id: user_id,
		    status: status
		})
	}).then(res => {
		if (res.ok)
		    return res.json()
		else
		    console.log("error");
		}).then(value => {
			var i;
			order=value.order
			var body=document.getElementById("body")
			var old_div=body.getElementsByTagName("div")
			for(od=0;old_div.length!=0;){
				body.removeChild(old_div[od])
			}
			for(i=0;i<order.length;i++){
				var div=document.createElement("div")
				div.setAttribute("id","order"+i) 
				div.setAttribute("class","order")
				var body=document.getElementById("body")
				body.appendChild(div)


				var detail=document.createElement("a")
				detail.setAttribute("id","detail") 
				detail.setAttribute("href","../order/"+order[i].order_id+"/?page=1&num=100") 
				var detail_node=document.createTextNode("查看订单细则")
				detail.appendChild(detail_node)
				div.appendChild(detail)

				var order_id=document.createElement("p")
				order_id.setAttribute("id","order_id") 
				var order_id_node=document.createTextNode("订单ID："+order[i].order_id)
				order_id.appendChild(order_id_node)
				div.appendChild(order_id)

				var number=document.createElement("p")
				number.setAttribute("id","number") 
				var number_node=document.createTextNode("订单编号："+order[i].number)
				number.appendChild(number_node)
				div.appendChild(number)

				var freight=document.createElement("p")
				freight.setAttribute("id","freight") 
				var freight_node=document.createTextNode("运费："+order[i].freight)
				freight.appendChild(freight_node)
				div.appendChild(freight)

				var paynumber=document.createElement("p")
				paynumber.setAttribute("id","paynumber") 
				var paynumber_node=document.createTextNode("支付宝交易号："+order[i].paynumber)
				paynumber.appendChild(paynumber_node)
				div.appendChild(paynumber)

				var cost=document.createElement("p")
				cost.setAttribute("id","cost") 
				var cost_node=document.createTextNode("订单总价："+order[i].cost)
				cost.appendChild(cost_node)
				div.appendChild(cost)

				var create_time=document.createElement("p")
				create_time.setAttribute("id","create_time") 
				var create_time_node=document.createTextNode("订单创建时间："+order[i].create_time)
				create_time.appendChild(create_time_node)
				div.appendChild(create_time)

				var pay_time=document.createElement("p")
				pay_time.setAttribute("id","pay_time") 
				var pay_time_node=document.createTextNode("订单付款时间："+order[i].pay_time)
				pay_time.appendChild(pay_time_node)
				div.appendChild(pay_time)

				var delivery_time=document.createElement("p")
				delivery_time.setAttribute("id","delivery_time") 
				var delivery_time_node=document.createTextNode("订单发货时间："+order[i].delivery_time)
				delivery_time.appendChild(delivery_time_node)
				div.appendChild(delivery_time)

				var deal_time=document.createElement("p")
				deal_time.setAttribute("id","deal_time") 
				var deal_time_node=document.createTextNode("订单成交时间："+order[i].deal_time)
				deal_time.appendChild(deal_time_node)
				div.appendChild(deal_time)

				var count=document.createElement("p")
				count.setAttribute("id","count") 
				var count_node=document.createTextNode("订单项数："+order[i].count)
				count.appendChild(count_node)
				div.appendChild(count)

				var name=document.createElement("p")
				name.setAttribute("id","name") 
				var name_node=document.createTextNode("收货人姓名："+order[i].name)
				name.appendChild(name_node)
				div.appendChild(name)

				var phone=document.createElement("p")
				phone.setAttribute("id","phone") 
				var phone_node=document.createTextNode("收货人电话："+order[i].phone)
				phone.appendChild(phone_node)
				div.appendChild(phone)

				var location=document.createElement("p")
				location.setAttribute("id","location") 
				var location_node=document.createTextNode("收货人地址："+order[i].location)
				location.appendChild(location_node)
				div.appendChild(location)

				var postcode=document.createElement("p")
				postcode.setAttribute("id","postcode") 
				var postcode_node=document.createTextNode("收货人邮编："+order[i].postcode)
				postcode.appendChild(postcode_node)
				div.appendChild(postcode)


		}
	})	
}