function doDel(num){  //num表示当前行
	var table = document.getElementById('tid');
	//console.log(num.parentNode.parentNode.rowIndex);
	//rowIndex tr的索引值   下标值  
	table.deleteRow(num.parentNode.parentNode.rowIndex);
	
	//table.deleteRow(1);
}


function doAdd(myform){
	//获取用户输入的信息   
	var id = myform.haha.value; 
	var name = myform.name.value;
	var age = myform.age.value;
	var sex = myform.sex.value;
	
	//获取table  form的内容要放到table中    
	var tables = document.getElementById('tid');
	//alert();
	var row = tables.insertRow(tables.rows.length);
	//tables.insertRow(6);
	row.insertCell(0).innerHTML = id;
	row.insertCell(1).innerHTML = name;
	row.insertCell(2).innerHTML = age;
	row.insertCell(3).innerHTML = sex;
	row.insertCell(4).innerHTML = "<button onclick=\"doDel(this)\">删除</button>";
	return false;//阻止顺着 form 提交出去 
}



