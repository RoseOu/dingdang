

function get_all(){
	fetch("http://120.24.4.254:5455/api/book/?category=0&page=1").then(function(res){
		if(res.ok){
		console.log("success")
			return res.json()
	 	}
		else
			console.log("error")
	}).then(res => {

		var i;
		book=res.book
		document.getElementById("text").innerHTML = book
		for(i=0;i<book.length;i++){
			// document.getElementById("text").innerHTML = book[i].book_id
			document.write(book[i].book_id+"<br />")
			document.write(book[i].name+"<br />")
			document.write(book[i].author+"<br />")
			document.write(book[i].selling_price+"<br />")
			document.write(book[i].introduction+"<br />")
			document.write(book[i].sale+"<br />")
			document.write(book[i].image+"<br />")
			document.write("<br />")
		}
	})	
}