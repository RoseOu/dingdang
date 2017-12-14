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

var now_url = window.location.href
var url_list = now_url.split('/')
var user_id = url_list[url_list.length-2]
var api_url = "http://120.24.4.254:5455/api/profile/"+user_id+"/"


//var id = cookie.getCookie('id');
var id = 2; //chrome关闭跨域时使用
fetch(api_url).then(function(res){
	if(res.ok){
	console.log("success")
		return res.json()
 	}
	else
		console.log("error")
}).then(res => {
	info=document.getElementById("info")

	var username=document.createElement("p")
	username.setAttribute("id","username") 
	var username_node=document.createTextNode(res.username)
	username.appendChild(username_node)
	info.appendChild(username)

	var email=document.createElement("p")
	email.setAttribute("id","email") 
	var email_node=document.createTextNode(res.email)
	email.appendChild(email_node)
	info.appendChild(email)

	var avatar=document.createElement("p")
	avatar.setAttribute("id","avatar") 
	var avatar_node=document.createTextNode(res.avatar)
	avatar.appendChild(avatar_node)
	info.appendChild(avatar)

	var birthday=document.createElement("p")
	birthday.setAttribute("id","birthday") 
	var birthday_node=document.createTextNode(res.birthday)
	birthday.appendChild(birthday_node)
	info.appendChild(birthday)

	var security_question=document.createElement("p")
	security_question.setAttribute("id","security_question") 
	var security_question_node=document.createTextNode(res.security_question)
	security_question.appendChild(security_question_node)
	info.appendChild(security_question)

})
