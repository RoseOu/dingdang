var showName = document.getElementById('showName');
var id = cookie.getCookie('id');
var logout = document.getElementById('logout');
id = 2; //chrome关闭跨域时使用
fetch('http://120.24.4.254:5455/api/profile/' + id).then(function(res){
	return res.json()
}).then(value => {
    console.log(value)
    showName.innerHTML = value.email;
})
logout.addEventListener('click',function(){
	cookie.delCookie("id");
	cookie.delCookie("token");
	cookie.delCookie("email");
	console.log(document.cookie)
})