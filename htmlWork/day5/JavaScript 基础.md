# JavaScript 基础  

* 引用方式 
* 语法关键词 保留字  
* 数据类型  

## 应用领域  

 * 页面的交互效果   比如轮播 选项卡   淘宝放大镜  
 * 页面的局部刷新  不需要手动刷新网页  比如股票网站 天气预报
 * vue.js react.js 
 * 混合app   webapp  

## 引用方式   

> js 是 JavaScript 的简称  只要你有浏览器  就可以运行js 

* 行内 

   ```
<a href="javascript:函数名" ">test</a>
<a href="#" onclick="alert('1234')">test</a>
   ```

* 内联    
  **可以放head 也可以放 body **  注意执行顺序问题

```
<script type="text/javascript">
			alert('123');
</script>
```



* 外链    

```
<script type="text/javascript" src="js/test.js"> 标签内部不能写内容 
</script>
```



## 语法

*  严格区分大小写     test  Text 
* 每一行语句结束的时候 必须加；
* 虽然js是弱类型语言  如果语句单独一行  var box=123 不加分号不报错  
* 但是 var box=123 var test=456； 这个时候box不加；分号就报错 

> 要求: 不管在不在一行上  只要语句结束  必须加分号 

### 标识符  

​	变量 、函数名字 、属性的名字 函数的参数 

标识符命名规则: 

 * 第一个字母必须是字母、下划线、$
 * 第一个字母不能是数字     1abc  错
 * 其它字符可以是字母数字下划线$
 * 不能用关键字 保留字 命名   

## 变量命名   

```
var test123;  只声明  不赋值  
alert(test123); 会弹出  undefined  未定义  

var test=123; 声明并赋值  
alert(test);

var box = test;隐式声明  将test的值赋给 box  
alert(box) #123
= 赋值的意思   

var a=123,b=456,c=789; 同时声明多个变量
```



## 注释   

```
// 单行注释    
/*多行注释*/
```



## js 内容输出方式

* alert()
  * 弹出字面量   alert(10)
    * 什么是字面量
      * 100 数值
      * 'libai' 字符串
      * null   空
      * true false  布尔
      * /js/
  * 弹出变量  
* document.write()  将内容输出到页面上  不弹窗  
*  console.log() 控制台显示   不显示在页面上 也不弹窗  一般程序员 测试常用   
* 每一行代码 结束 加 ；号

## 错误类型

```
Uncaught SyntaxError: Invalid or unexpected token   语法错误   
404 找不到的意思  你的文件引入路径有问题 导致找不到  
Uncaught ReferenceError: kangbazi is not defined 变量不存在 
```



  ## 数据类型   

* undefined  未定义
* null   空
* boolean 布尔类型
* string  字符串 
* number 类型
* object 类型 对象  
* function类型   
* typeof  查看数据类型   

### typeof  写法   typeof 空格 变量名 

```
var test = 123;
test = '123';
console.log(typeof test) 返回 number 
console.log(typeof test) 返回 string
```

### undefined   

```
var test; 这个叫只声明 没有赋值  赋值也叫做初始化  console.log(test);返回 undefined   
console.log(kangbazi);返回 Uncaught ReferenceError: kangbazi is not defined

```

> 未初始化 、不存在的变量区别:
>
> 未初始化是声明了 但是没有赋值  
>
> 不存在就是 直接没声明

### null 是一个特殊的对象（object）类型  

```
var box = null;
console.log(typeof box);返回 object

一般用它来做判断用 

var box = null;
if(box != null){
alert('对象已经存在');
}else{
alert('对象不存在');
}
```

> undefined 是从null 派生出来的   
>
> = 赋值  == 值相等 返回的结果是 true 和false   === 表示值和类型都相等 true 和false 
>
> var test = 123;
>
> var box = '123';
>
> test == box  true
>
> test === box  false
>
>  var box; //undefined
>  var test = null; //null
>  console.log(undefined == null); //true

### boolean类型 

两个字面量  true 和false  true 不一定等于1  false 不一定等于0   js 严格区分大小写  true和false 必须是小写  

True Flase 都不是 boolean 类型的值    

```
var box = true;
console.log(typeof box); 返回boolean 


var test = 'hello,world';
var test1 = Boolean(test);
alert(typeof test); string
alert(typeof test1); boolean 
其它类型的都可以通过  Boolean转化为 boolean类型  
		var test = 'hello'; 执行true
		var test = '';  空字符串 执行false 
		第一步首相将 test 由string类型转化成boolean类型 
		if(test){
			alert('如果条件为true执行我');
		}else{
			alert('如果条件为false 执行我');
		}
```

其它类型转成 boolean 类型的规则     **重要 **

| 数据类型  | 转成true的情况          | 转成false的情况        |
| --------- | ----------------------- | ---------------------- |
| boolean   | true                    | false                  |
| string    | 任何非空字符串          | 空字符串               |
| number    | 任何非零数值 包括无穷大 | NaN (not a number)、 0 |
| object    | 任何对象                | null                   |
| undefined |                         | undefined              |
|           |                         |                        |



### number类型   

number包含两周类型:

 * 整型  
 * 浮点型   

```
var box = 100; 最基本的数值字面量 是十进制的整数    

二进制  0~1 
八进制  0~7 
16进制  0~9 A~F 
十进制 0~9 
```

### 八进制整数 在js中 0开头的表示八进制    

```
var box = 017;
var box = 070; 56
box = 08;    无效八进制  直接返回8 
box = 010;   返回8
```

### 十六进制 以 0x开头   

```
var box  = 0xA; 返回10
		  0x1f；返回31
```

### 浮点类型 最高精度 17位  算术运算不是100%精确  

> console.log(0.1+0.2) //0.30000000000000004  写代码的时候 注意判断一下  

```
	var box = 8.17;
    box	=  .8; 不爆错 但是 不能这么写 
    
    var box = 8.16e10;//相当于 8.16乘以 10的10次方     指数次幂 
	box = 8.16e-5;
	
	查看浮点类型的范围   
		alert(Number.MAX_VALUE); 最大值
		alert(Number.MIN_VALUE); 最小值  
		
	var box = 100e1000; //Infinity 无穷大 
	    box = -100e1000; //-Infinity 无穷小 
	    
		var box = 100e1000;
		alert(box < Number.MAX_VALUE);
		

```

### NaN

```
var box = 0/0;
alert(box);  //NaN
var box = 10/0;  //Infinity 
var box = 10/0*0;  //NaN

alert(Number.NaN);  //NaN

任何与NaN运算的结果肯定是 NaN 
alert(NaN+1); //NaN

alert(NaN == NaN); //NaN自己也不相等   返回false 

判断一个值 是否是NaN 系统提供了一个函数    isNaN() 是NaN返回true  'abc' 否则false 123   

alert(isNaN('123'));//'123'可以转成数值123 所以不是NaN 返回false
alert(isNaN('abc')); // abc不能转化成数值 所以是NaN 返回true 
alert(isNaN(true));//因为 true 会转化成1 1不是NAN 所以返回false 
alert(isNaN(NaN));//返回true

		
```



### 非数值 转成数值  

* Number()     注意大小写
* parseInt()
* parseFloat()

#### Number()

```
alert(Number(true));//1
alert(Number('123'));//123
alert(Number(null));//0
alert(Number(undefined)); //NaN*/
alert(Number(25));//25
alert(Number('070'));//70 去掉0
alert(Number('456'));//456
alert(Number('08.90'));//去掉0 8.9 
alert(Number(''));//0*/
alert(Number('abc123'));//NaN
alert(Number('123abc'));//NaN 
```

#### parseInt()

```
console.log(parseInt('0xA')); //10
console.log(parseInt('AF')); //NaN
console.log(parseInt('AF',16)); //175
console.log(parseInt('0xAGao'));//Gao给多虑掉了 10
console.log(parseInt('123ABC'));//123 ABC被过滤掉
console.log(parseInt('ABC123'));//开始是个ABC 就停止 直接返回NaN
console.log(parseInt('123ABC123'));//123到ABC就停止  
console.log(parseInt('12.13'));//12 遇到.停止 
console.log(parseInt(''));//NaN
console.log(parseInt('070'));//70
console.log(parseInt('101010'));//101010
console.log(parseInt('101010',2));//42 以2进制转化 最后转成10进制 
console.log(parseInt('070',8));//56
```


#### parseFloat()

```
console.log(parseFloat('123abc'));//123
console.log(parseFloat('0xA'));//0 不认16进制 
console.log(parseFloat('12.3.4'));//12.3
console.log(parseFloat('0123.45'));//123.45 0忽略掉
console.log(parseFloat('1.23e7'));//12300000
```



### string类型 字符串    

> 原字符串永不改变  会生成新的结果给你   

* 单引号 ''
* 双引号    “”
* 单引号包裹双引号  双引号包裹单引号  绝对不能穿插使用        

```
var box = '123';
    box = "test";效果一样 
    test = ' "str"';
    '" 报错 
```



| 特殊字符 | 说明 |
| -------- | ---- |
| \n       | 换行 |
| \b       | 空格 |
| \r       | 回车 |
| \t       | 制表 |
|          |      |



#### 拼接字符串  +   

```
var test = 'kangbazi';
test = test + "1806";
console.log(test);
```



#### 值转化成字符串    

> 变量.toString() undefined null  报错

```
var box = true;
console.log(typeof box); //boolean
console.log(typeof box.toString()); //string 
alert(typeof box.toString());//10
console.log(box.toString(2)); //先将10转成2进制然后转成字符串
console.log(box.toString(8));//12
console.log(box.toString(10));//10
console.log(box.toString(16));//a
```



String(变量) 任意类型都可以转化  包括 undefined null

```
var box;
//console.log(box.toString()); //报错
console.log(String(box));//undefined

var test=null;
//console.log(test.toString()); //保存 
console.log(String(test)); //null
```





## object 类型  

> 数组和对象 统称为  object  
>
> var test = [1,2,3,4,5];
> alert(typeof test);//object 

```
var box = new Object();

var box = new Object(10);//对象类型 值是10
var age = box + 100;
console.log(age);  //110
```

* new Object()
* new Number()
* new String()
* new Boolean()

```
		var box = new Number();
		console.log(typeof box);
		
		var box1 = new String();
		console.log(typeof box1);
		
		var box2 = new Boolean();
		console.log(typeof box2);
```



> 以上知道对象是这么命名  就可以  后期又详细的解释   



数据类型分类: 

 * 基本类型 
    * string  number boolean  undefined  null function  栈内存中  
 * 引用类型  
    * object      堆内存中 



## 运算符   

* 表达式  
* 一元运算符
* 算术运算符 
* 逻辑运算符 
* 关系运算符  
* 位运算符  
* 赋值运算符  
* 其它运算符 
* 优先级   

### 表达式   

​	就是字面量 或者变量    

```
56 
true 
'abc'
//正则表达式   
var box；

box + 1 
typeof(box)
box>100 

```

### 一元运算符  

```
var box =100;
box++ 相当于  box = box+1；
++box;
box++;
--box;
box--;

var box = 100;
box = box +１;
console.log(box++);//100       101
console.log(++box);//102       102 
console.log(box--);//102       101
console.log(--box);//100	   100
```

#### 前置运算 先赋值  后运算   

```
box++; 
box--;
```

#### 后置运算    先运算  后赋值 

```
++box;
--box;
```

思考？

```
var a=10;
var b=a++---a;
console.log(a);
console.log（b）；
第一步:先赋值a  也就是把10先拿出来   
第二步:a+1     a的值变成了 11 
第三步 先运算a-1 a的值变成了 10  
第四步 : 将拿出来的10 - 10 
结果0 
```

```
var a=5;
b = ++a + a++; b=12
	6     6    a = 7
c = b-- - --b;   b=10 c=2
	12    10  
```

#### 其它类型 一元运算符的应用   

```
var box = '123';//先把字符串转化成数值 
box = 'abc';   //NaN
box = false; //将false转化成0
box = 1.2; 


+
var box=100;
box='100'; //先把100转成数值
box='abc';//NaN
console.log(+box);

-

var box=100;
//box='100'; //先把100转成数值
//box='abc';//NaN
console.log(-box);
```

### 算术运算符 true 转为1 false 0  空字符串转化为 0  null 0    

NaN跟任何值运算 都得NaN 

```
1+2 
1+NaN //NaN
Infinity+Infinity //Infinity
-Infinity-Infinity//-Infinity
Infinity+-Infinity //NaN 

var box = 'test';
console.log(100+box); //只要有字符串 就是拼接  100test
box='100';
console.log(100+box); //100100 由字符串就不是加法 
console.log('您的余额是'+10+2000);//您的余额是102000
console.log('您的余额是'+(10+2000));//您的余额是2010
console.log(10+2000+'您的余额');//2010您的余额


	var box = new Object();
	console.log(100-true);//99 将true转化为1 
	console.log(100-'');//100将空字符串转化为0
	console.log(100-'60');//40 将字符串60 转为60 
	console.log(100-box);//NaN
```

### 关系运算符 返回的结果是boolean类型    

| 运算符 | 说明 |
| ------ | ---- |
| >      |      |
| <      |      |
| =      |      |
| !=     |      |
| >=     |      |
| <=     |      |
| ==     |      |
| ===    |      |
| !==    |      |



```
console.log(undefined == null);//true
console.log('NaN'== NaN);//false
console.log(5== NaN);//false
console.log(NaN== NaN);//false
console.log(0 == false);//true
console.log(1 == true);//true
console.log(0 == undefined);//false
console.log(0 == null);//false
console.log(1 == '1');//true
console.log(1 === '1');//false
```



### 逻辑运算符  

* &&   逻辑与  and 
* ||    逻辑或 or 
* ！  逻辑非 not



#### 逻辑与  表达式1 && 表达式2  两边表达式的结果都是true 返回true  有一个false 最终结果false  记住 

> var box = (3>4) && (5>3);
>
> console.log(box); //false 



```
var box = new Object();
console.log(box && (5>4)); //true 第一个是对象的时候 返回第二个操作数 
console.log((5<4)&& box);//[object Object] 第二个操作数是对象 如果第一个为true 则返回第二个对象 如果第一个为false 直接返回false
console.log((5<4)&& null);//false   
了解 
```



#### 逻辑或  (5>3) || (3<4);  true 两边表达式 只要有一个为真  最终结果就是真   两个都为假 最终才是假   记住 重要  

```
var box = new Object();
console.log(box || (3>4));//[object Object]
console.log((3>4)|| box );//[object Object]
console.log((3<4)|| box );//true
console.log(null|| null);//null
console.log(undefined|| undefined );//undefined

了解 
```



#### 逻辑非  ！

```
var box = !(5>4);
var test = new Object();
console.log(box);//false
console.log(!'');//true
console.log(!'abc');//false
console.log(!null);//true
console.log(!undefined);//true
console.log(!NaN);//true
console.log(!0);//true
console.log(!test);//false
console.log(!!0);//!!跟没写一样一样的
```

#### 位运算符  了解    

> 先转成2进制    
>
> 位与   两个都是1  得1  有一个0 得0   
>
> 位或 有一个1就是1 都是0 得 0 



#### 赋值运算符   

> = 

+=

-=

*=

/+

%=

```
var box=100;
box +=10; //box = box+10;
box -= 10; //box = box-10;
console.log(box);
```

#### 其它运算符  

```
, 逗号运算符
var box = [1,2,3];
var a=1,b=2,c=3;
```

##### 三元运算符   也叫三目运算符 很重要   

```
var box = 5;
if（box>4）{
    alert('对');
}else{
    alert('错');
}
(5>4)?'对':'错';
表达式?'1'：'2';
？前面表达式如果为真选择:前面的  如果为假 选择 :后面的
```

#### 优先级  

```
()[]   > 
一元运算符(++ --)   >    
乘法除法求余 >   
== !== !== ===     >
&&    >  
|| >
?： > 
赋值=  >
   ,
```





## 流程控制语句  

* if  else  
* switch 
* do while 
* while 
* for 
* for in 
* with 
* break continue 

### if else 

```
if（50>40）alert('真');
if(50>40)
   alert('真');
if(表达式){
    业务逻辑
}


var box = 100;
if(box >=100){
alert('状元')
}else if(box >=90){
alert('榜眼');
}else if(box >=80){
alert('探花');
}else if(box >=70){
alert('秀才');
}else if(box >=60){
alert('进士');
}else{
alert('各回各家');
}
```



#### switch 

```
switch (表达式){
		case 结果:
			break;
		default:  相当于if 里边的else 
			break;
	}
	
var box=80;
	switch (box){  结果只能是 100 90 80 70 60 除了这个五个 走 default 
		case 100:
			console.log('状元');
			break; 防止向下穿透 遇到break 跳出所有循环
		case 90:
			console.log('榜眼');
			break;
		case 80:
			console.log('探花');
			break;
		case 70:
			console.log('进士');
			break;
		case 60:
			console.log('举人');
			break;
		default: 相当于我们if elseif  else 中的  else  
			console.log('落榜');
			break;
	}
```



## for 循环  

```
var box = 1;
if(box <=5 ){
box++;
console.log(box); //2  这种情况只能出来1个值
}
需求是: 
1 2 3 4 5 启用for 
for(var box=1;box<=5;box++){
console.log(box);
}
```



作业  

1.有边框的九九乘法表   正立 倒立  

2.金三角 正立 倒立   *

3.菱形 