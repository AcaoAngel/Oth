
# 	<head>
# 		<title>OTH-Omataloushallinta</title>
# 		<meta charset="utf-8">
# 		<meta name= "viewport" content= "width=device-width, initial-scale=1.0"> 
# 		<link rel="stylesheet" type="text/css" href="{% static 'CSS/styles.css' %}">   
# 		<link rel="stylesheet" type="text/css" href="{% static ' font-awesome-4.7.0/css/font-awesome.min.css' %}">
# 		<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
# 		<link rel="preconnect" href="https://fonts.gstatic.com/"> 
# 		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
# 		<script src="https://kit.fontawesome.com/a076d05399.js"></script>
# 	</head> 
    
# <!DOCTYPE html>
# <html>    
# <head>
# 	<title>Luo tili</title>
# 	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
# 	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
# 	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">
   
# 	<style>
		
# 		.user_card {
#             width: 350px;
#             height: 820px;
# 			margin-top: 5px;
#             margin-bottom: auto;
#             margin-left: -1800px;
# 			background: #090a0a;
# 			position: relative;
# 			display: flex;
# 			justify-content: center;
# 			flex-direction: column;
# 			padding: 10px;
# 			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
# 			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
# 			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
# 			border-radius: 5px;
#             z-index: 999;
            
# 		}

#         .justify-content-center h3{
#             margin-top: -50px;
#         }

#         .libele{
#             color: azure;
#         }

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} Movements {% endblock %}</title>

	<title>Minun tili</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">
  
	<style>

		.user_card {
			width: 300px;
			margin-top: 170px;
            margin-bottom: auto;
            margin-left: -1800px;
			background: #090a0a;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 5px;
            z-index: 999;
		}


		.not-account{
          
            margin-top: -25px;
            background-size: 50px;
			
		}

        .login_btn{
            font-family: 'Kenia', cursive;
            font-size: 20px ;
            background-size: 70px;

# 	</style>
      }


        .user_card h3{
            color: rgb(255, 15, 15) !important;
            margin-top: 30px;
			font-family: 'Kenia', cursive;
		}

	</style>

# </head>
# <body>
# 	<div class="container h-100">
# 		<div class="d-flex justify-content-center h-100">
# 			<div class="user_card">
# 				<div class="d-flex justify-content-center">
                    
#                          <h3 id="form-title">Luo tili </h3>
                    
# 				</div>
# 				   <div class= 'libele'>
#                         <form action="/create_account/" method="POST" ,="" enctype="multipart/form-data">
                           
#                             <input type="hidden" name="csrfmiddlewaretoken" value="lSURBeNoV0AJ3ZjyhhONNT6b0w4wc3o8JxT4eTsMnj8FyVHmCICoGXolTni5Q2Mh">
#                             {% csrf_token %}
                       

              
#                         <tr><th><label for="id_user">User:</label></th><td><select name="user" required id="id_user">
                        
#                         <option value="" selected="">---------</option>
                      
         
#                       </select>
#                             <hr>
                        
#                             <label><label for="id_account_name">Account name:</label></label>
#                             <input type="text" name="account_name" maxlength="100" required="" id="id_account_name">
#                             <hr>
                        
#                             <label><label<label for="id_account_value">Account value:</label></label>
#                             <input type="number" name="account_value" step="0.01" required="" id="id_account_value">
#                             <hr>
                        
#                              <label><label for="id_info">Info:</label></label> 
#                             <label><label for="id_info">Info:</label></label>
                            
#                             <textarea name="info" cols="40" rows="7" maxlength="500" required="" id="id_info">Default info text</textarea>
#                             <hr>

#                             <label><label for="id_save_percent">Save percent:</label></label>
#                             <input type="number" name="save_percent" value="10" step="0.01" required="" id="id_save_percent">
#                             <hr>
                        
#                             <label><label for="id_saving_time">Saving time:</label></label>
#                             <input type="number" name="saving_time" value="12" required="" id="id_saving_time">
#                             <hr>
                        
#                         <input type="submit" class="btn btn-primary" value="Save">
#                         </form>
#                 </div>
 
#             </div>

#         </div>


#     </div>

# </div>
# </div>
</head>
<body>


<h1>My accounts</h1>

{% for user_accounts in object_list %}
<ul>
    <li><a href="{% url 'accounts:account_detail' user_accounts.id %}">{{user_accounts.account_name}} Amount: {{user_accounts.account_value}}</a></li>
</ul>
{% empty %}





<div class="container h-100">
	<div class="d-flex justify-content-center h-100">
		<div class="user_card">
			<div class="d-flex justify-content-center">
				<h3 id="form-title"> Ei ole vielä tili</h3>
			</div>
		<div class="d-flex justify-content-center form_container">
			<form method="POST" action="">
				{% csrf_token %}
				<div class="input-group mb-3">
					<div class="d-flex justify-content-center mt-3 login_container">
						<div class="not-account">
							<a href="{% url 'accounts:create_account' %}" class="btn login_btn" role="button">Luo uusi tili</a> 
						</div> 
					</div>
				</div>
			</form>

		</div>
		</div>
	</div>
</div>
{% endfor %}

</body>
</html>

























		
		.main{
			margin-top: 60px;
			max-width: 1000px; width: 100%; padding: 10px;
			background-color: rgb(228, 237, 252);
			height: min-content;
			margin-left: 250px;
		}

		.jss629.jss625 {
    transform: translateY(-50%) rotate(180deg);
}
.jss629:hover {
    background-color: transparent;
}
.jss630:hover {
    background-color: rgba(0, 0, 0, 0.08);
}
.jss629 {
    top: 50%;
    right: 8px;
    color: #4A4A4A;
    position: absolute;
    transform: translateY(-50%) rotate(0deg);
    transition: transform 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}

.jss630 {
    flex: 0 0 auto;
    color: rgba(0, 0, 0, 0.54);
    padding: 12px;
    overflow: visible;
    font-size: 1.5rem;
    text-align: center;
    transition: background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    border-radius: 50%;
}
.jss27 {
    color: inherit;
    border: 0;
    margin: 0;
    cursor: pointer;
    display: inline-flex;
    outline: none;
    padding: 0;
    position: relative;
    align-items: center;
    user-select: none;
    border-radius: 0;
    vertical-align: middle;
    justify-content: center;
    -moz-appearance: none;
    text-decoration: none;
    background-color: transparent;
    -webkit-appearance: none;
    -webkit-tap-highlight-color: transparent;
}
.jss624 {
    display: flex;
    padding: 0 24px 0 24px;
    min-height: 48px;
    transition: min-height 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    font-weight: bold;
    border-radius: 4px;
    background-color: #E8E8E8;
}
.jss635 {
    width: 100%;
    display: flex;
    align-items: inherit;
    justify-content: inherit;
}
svg:not(:root) {
    overflow: hidden;
}

.jss30 {
    fill: currentColor;
    width: 1em;
    height: 1em;
    display: inline-block;
    font-size: 24px;
    transition: fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    user-select: none;
    flex-shrink: 0;
}

	<div role='main' class='main'>
		<div class= 'ConsumptionView_root_3cR'>

			<div class="jss27 jss630 jss629 jss625" tabindex="-1" role="button" aria-hidden="true">
				<span class="jss635">
					<svg class="jss30" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="presentation">
						<path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path>

						
						<path fill="none" d="M0 0h24v24H0z"></path>
					</svg>
				</span>
				<span class="jss706"></span>
			</div>

			<h1>Tilini tilanne</h1>

			{% for user_accounts in object_list %}
			<ul>
    			<li><a href="{% url 'accounts:account_detail' user_accounts.id %}">{{user_accounts.account_name}} Amount: {{user_accounts.account_value}}</a></li>
			</ul>
			{% empty %}




			</div>	
		</div>
	</div>




--------------------------------------------------


<!-- </head>
<body>
	<h1>My accounts</h1>
	<div role='main' class='main'>
		<div class= 'ConsumptionView_root_3cR'>
			<li class="dropdown">
				<a href="#" style="text-decoration: none" class="dropdown-toggle" data-toggle="dropdown">Tilanne

				<span class="caret"></span>
				
		   		</a>
		   
				<ul class="dropdown-menu">
					<li>{% for user_accounts in object_list %}
					<a href="{% url 'accounts:account_detail' user_accounts.id %}">{{user_accounts.account_name}} Amount: {{user_accounts.account_value}}</a> 
					<br>{% empty %}</li>
				</ul>
	  		</li>
		</div>
	</div>
 -->


-------------------------------------------
		.dropdown-toggle[aria-expanded="true"]:after {
transform: rotate(180deg); 
}
/*for animation*/ 
.dropdown-toggle:after { 
transition: 0.7s; 
}

</head>
<body>
	<h1>My accounts</h1>
	<div role='main' class='main'>
		<div class= 'ConsumptionView_root_3cR'>
			<li class="dropdown">
				<a href="#" class="dropdown-toggle" data-toggle="dropdown"> Tilanne <span class="caret"></span></a> 

		   
				<ul class="dropdown-menu" role="menu">
					<li>{% for user_accounts in object_list %}
					<a href="{% url 'accounts:account_detail' user_accounts.id %}">{{user_accounts.account_name}} Amount: {{user_accounts.account_value}}</a> 
					<br>{% empty %}</li>
				</ul>
	  		</li>
		</div>
	</div>
----------------------------------------


{% extends "base.html" %}

{% block body %}
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} Movements {% endblock %}</title>

	<title>Minun tili</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">
  
	<style>

.tabs{

position: absolute;
top:50%;
left: 50%;
transform: translate(-50%, -50%);
width: 1200px;
height: min-content;
background: #eee;
overflow: hidden;
box-shadow: 2px 2px 5px 2px #ccc;
  
display:flex;
}
		.user_card {
			width: 300px;
			margin-top: 170px;
            margin-bottom: auto;
            margin-left: -1800px;
			background: #090a0a;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 5px;
            z-index: 999;
		}


		.not-account{
          
            margin-top: -25px;
            background-size: 50px;
			
		}

        .login_btn{
            font-family: 'Kenia', cursive;
            font-size: 20px ;
            background-size: 70px;

      }


        .user_card h3{
            color: rgb(255, 15, 15) !important;
            margin-top: 30px;
			font-family: 'Kenia', cursive;
		}

	</style>

</head>
<body>

<div class ="tabs">
	<div class="tab">
 		{% for user_accounts in object_list %}
		<ul>
    		 <li><a href="{% url 'accounts:account_detail' user_accounts.id %}">{{user_accounts.account_name}} Amount: {{user_accounts.account_value}}</a><br>{% empty %} </li> -->
		  </ul> 
		</div> 

	
		  
		 
		  

<div class="container h-100">
	<div class="d-flex justify-content-center h-100">
		<div class="user_card">
			<div class="d-flex justify-content-center">
				<h3 id="form-title"> Ei ole vielä tili</h3>
			</div>
		<div class="d-flex justify-content-center form_container">
			<form method="POST" action="">
				{% csrf_token %}
				<div class="input-group mb-3">
					<div class="d-flex justify-content-center mt-3 login_container">
						<div class="not-account">
							<a href="{% url 'accounts:create_account' %}" class="btn login_btn" role="button">Luo uusi tili</a> 
						</div> 
					</div>
				</div>
			</form>

		
		</div>
		</div>
	</div>
</div>

{% endfor %} 


</body>
</html>


{% endblock %}













#                          <input type="hidden" name="csrfmiddlewaretoken" value="lSURBeNoV0AJ3ZjyhhONNT6b0w4wc3o8JxT4eTsMnj8FyVHmCICoGXolTni5Q2Mh"> 
#                             {% csrf_token %}
                       

             
#                        <tr><th><label for="id_user">User:</label></th><td><select name="user" required id="id_user">
                        
#                         <option value="" selected="">---------</option> 
                      
         
#                       </select> 
#                             <hr>
                        
#                             <label><label for="id_account_name">Account name:</label></label>
#                             <input type="text" name="account_name" maxlength="100" required="" id="id_account_name">
#                             <hr>
                        
#                             <label><label<label for="id_account_value">Account value:</label></label>
#                             <input type="number" name="account_value" step="0.01" required="" id="id_account_value">
#                             <hr>
                        
#                              <label><label for="id_info">Info:</label></label> 
#                             <label><label for="id_info">Info:</label></label>
                            
#                             <textarea name="info" cols="40" rows="7" maxlength="500" required="" id="id_info">Default info text</textarea>
#                             <hr>

#                             <label><label for="id_save_percent">Save percent:</label></label>
#                             <input type="number" name="save_percent" value="10" step="0.01" required="" id="id_save_percent">
#                             <hr>
                        
#                             <label><label for="id_saving_time">Saving time:</label></label>
#                             <input type="number" name="saving_time" value="12" required="" id="id_saving_time">
#                             <hr>
                        
#                         <input type="submit" class="btn btn-primary" value="Save">
#                         </form>
#                 </div>
 
#             </div>

#         </div>


#     </div>

# </div>
# </div>




# sdfsd sdf sdf sdf dsf sdf 






<!-- 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   

	<title>Minun tili</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">
  
	<style>

		.user_card {
			width: 300px;
			margin-top: 170px;
            margin-bottom: auto;
            margin-left: -1800px;
			background: #090a0a;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 5px;
            z-index: 999;
		}


		.not-account{
          
            margin-top: -25px;
            background-size: 50px;
			
		}

        .login_btn{
            font-family: 'Kenia', cursive;
            font-size: 20px ;
            background-size: 70px;

      }


        .user_card h3{
            color: rgb(255, 15, 15) !important;
            margin-top: 30px;
			font-family: 'Kenia', cursive;
		}

	</style>

</head>
<body>


<h1>My accounts</h1>

{% for user_accounts in object_list %}
<ul>
    <li><a href="{% url 'accounts:account_detail' user_accounts.id %}">{{user_accounts.account_name}} Amount: {{user_accounts.account_value}}</a></li>
</ul>
{% empty %}





<div class="container h-100">
	<div class="d-flex justify-content-center h-100">
		<div class="user_card">
			<div class="d-flex justify-content-center">
				<h3 id="form-title"> Ei ole vielä tili</h3>
			</div>
		<div class="d-flex justify-content-center form_container">
			<form method="POST" action="">
				{% csrf_token %}
				<div class="input-group mb-3">
					<div class="d-flex justify-content-center mt-3 login_container">
						<div class="not-account">
							<a href="{% url 'accounts:create_account' %}" class="btn login_btn" role="button">Luo uusi tili</a> 
						</div> 
					</div>
				</div>
			</form>

		</div>
		</div>
	</div>
</div>
{% endfor %}

</body>
</html>

 



.tabs{

position: absolute;
top:50%;
left: 50%;
transform: translate(-50%, -50%);
width: 1200px;
height: min-content;
background: #eee;
overflow: hidden;
box-shadow: 2px 2px 5px 2px #ccc;
  
display:flex;
}



--------------------------


<div class ="tabs">
		<div class="tab">
			{% for user_accounts in object_list %}
			<ul>
				 <li><a href="{% url 'accounts:account_detail' user_accounts.id %}">{{user_accounts.account_name}} Amount: {{user_accounts.account_value}}</a><br>{% empty %} 
			  </ul> 
			</div> 
	
</div>
	

	--------------

	
	

<div class ="tabs">
	<div class="tab">
	
		
			

				{% for user_accounts in object_list %}
				<ul>
				<button class="open-button" onclick="openForm()">{{user_accounts.account_name}} Amount: {{user_accounts.account_value}}</button>
			</ul>
		
				
			
					
			</form>
	


			<div class="form-popup" id="myForm">
				<form action="account_detail.php" class="form-container">
			<ul>
				{% include "account_detail.html" %}
			  </ul> 
		
				
		</form>
	</div>


		
	<script>
		function openForm() {
		  document.getElementById("myForm").style.display = "block";
		}
		
		function closeForm() {
		  document.getElementById("myForm").style.display = "none";
		}
		</script>


--------------------------------------

account form



{% extends "base.html" %}

{% block title %} Accounts {% endblock %}

{% block body %}

    
<!DOCTYPE html>
<html>    
<head>
	<title>Luo tili</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">
   
	<style>
		
		.user_card {
            width: 400px;
            height: 650px;
			margin-top: 20px;
            margin-bottom: 30px;
            margin-left: -1800px;
			background: #090a0a;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 1rem;
            z-index: 999;
            border: 2px solid rgba(255,255,255,0.2);
           

            
		}

        .justify-content-center h3{
          
            margin-top: 10px;
            font-size: 35px;
            margin-right: 5px;
            font-family: 'Kenia', cursive;
            font-weight:bold;
        }

        .libele{
            color: azure;
            margin-left: 20px;
            margin-top: 20px;
            font-family: 'Kenia', cursive;
            font-size: 15px;
        }
        .libele label{
           
           margin-left: 0px;
           margin-right: 50px;
           width: 70px;
           height: 24px;
       }

       textarea{
           width: 340px;
       }
       .btn-primary{
           background: #0e24a0 !important;
           color: white !important;
           margin-top: -20px;
           margin-left: 267px;
           font-size: 20px;
           font-weight:bold;
       }
	</style>
</head>
<body>

	<div class="container h-100">
		<div class="d-flex justify-content-center h-100">
			<div class="user_card">
				<div class="d-flex justify-content-center">
                    
                    <h3 id="form-title">Luo tili</h3>
                    {{form.errors}}
                </div>
                <div class= 'libele'>
                    <form action="/create_account/" method="POST" ,="" enctype="multipart/form-data">  
                              <!-- <input type="hidden" name="csrfmiddlewaretoken" value="lSURBeNoV0AJ3ZjyhhONNT6b0w4wc3o8JxT4eTsMnj8FyVHmCICoGXolTni5Q2Mh">  -->
                        {% csrf_token %}
                                
                        {% for field in form %}
                            <label>{{ field.label_tag }}</label>
                            {{ field }}
                            <hr>
                            {% endfor %}
                    </form>
                        <input type="submit" class="btn btn-primary" value="Save">
                </div>    
			</div>
        </div>

    </div>


</body>
</html>  


                               
                 
                           <!-- <tr><th><label for="id_user">User:</label></th><td><select name="user" required id="id_user">
                            
                            <option value="" selected="">---------</option> 
                          
             
                          </select> 
                                <hr>
                            
                                <label><label for="id_account_name">Account name:</label></label>
                                <input type="text" name="account_name" maxlength="100" required="" id="id_account_name">
                                <hr>
                            
                                <label><label<label for="id_account_value">Account value:</label></label>
                                <input type="number" name="account_value" step="0.01" required="" id="id_account_value">
                                <hr>
                            
                                 <label><label for="id_info">Info:</label></label> 
                                <label><label for="id_info">Info:</label></label>
                                
                                <textarea name="info" cols="40" rows="7" maxlength="500" required="" id="id_info">Default info text</textarea>
                                <hr>
    
                                <label><label for="id_save_percent">Save percent:</label></label>
                                <input type="number" name="save_percent" value="10" step="0.01" required="" id="id_save_percent">
                                <hr>
                            
                                <label><label for="id_saving_time">Saving time:</label></label>
                                <input type="number" name="saving_time" value="12" required="" id="id_saving_time">
                                <hr> -->

 {% endblock %}


















                    <!-- <body>
                        <div>
                            <form action="/create_account/" method="POST", enctype="multipart/form-data">
                                {% csrf_token %}  -->
                                {{form.as_table}}
                                {% for field in form %}
                                    <label>{{ field.label_tag }}</label>
                                    {{ field }}
                                    <hr>
                                {% endfor %}
                                <input type="submit" value="Save">
                            </form>
                        </div>
                    </body>  
                    
                   




   -----------------------

   account account_detail

          {% extends "base.html" %}






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h2>Account information</h2>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">
   

    {% block title %} Movements {% endblock %}


{% block body %}


	<style>
		
		.user_card {
            width: 700px;
            height: min-content;
			margin-top: 90px;
            margin-bottom: 30px;
            margin-left: -1800px;
			background-color: #9ABBFB;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 1rem;
            z-index: 999;
            border: 2px solid rgba(255,255,255,0.2);
            box-shadow: 2px 2px 5px 2px #ccc; 
            display:flex;

            
		}

        
        #form-title{
            color: #042496;
            margin-top: -10px;
            font-size: 35px;
            margin-right: 5px;
            font-family: 'Kenia', cursive;
            font-weight:bold;
      }

      .libele{
            color: #042496;
            margin-left: 20px;
            margin-top: 40px;
            font-size: 15px;
            font-family: 'Kenia', cursive;
        }

        .libele a{
            color: #041657;
           
            font-size:20px;
            font-weight:bold;
            font-family: 'Kenia', cursive;
        }
        
	</style>
</head>
<body>

    <body>
    

        <div class="container h-100">
            <div class="d-flex justify-content-center h-100">
                <div class="user_card">
                    <div class="d-flex justify-content-center">
                        
                        <h3 id="form-title">Account information</h3>
                      
                    </div>
                    <div class= 'libele'>

        <ul>
            <li style="font-weight: bold;">{{account.account_name}}</li>
            <li style="font-weight: bold;">{{account.account_value}}</li>
            <li style="font-weight: bold;">{{account.info}}</li>
            <li style="font-weight: bold;">{{account.save_percent}}</li>
            <li style="font-weight: bold;">{{account.saving_time}}</li>
        </ul><hr>
        <h2>Movements</h2>
        {% for i in movements %}
        <ul>
            <li style="font-weight: bold;">{{i.date.date}}  |  Event: {{i.event}}  |  Amount: {{i.amount}}  |  Saldo after movement: {{i.account_value_after}}</li>
        </ul>
        {% endfor %}
    
        <hr>
    
        <a href="{% url 'accounts:pay_form' %}">Insert new payment</a><br>
        <a href="{% url 'accounts:movements_form' %}">Move to own account</a><br>
        
    </div>
</div> </div>
</div>

    </body>
    {% endblock %}
    
    </html>
    
    
    
    
    
    
    
























    <!-- <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
       
    </head>
   
    <body>
        <h2>Account information</h2>
        <ul>
            <li style="font-weight: bold;">{{account.account_name}}</li>
            <li style="font-weight: bold;">{{account.account_value}}</li>
            <li style="font-weight: bold;">{{account.info}}</li>
            <li style="font-weight: bold;">{{account.save_percent}}</li>
            <li style="font-weight: bold;">{{account.saving_time}}</li>
        </ul><hr>
        <h2>Movements</h2>
        {% for i in movements %}
        <ul>
            <li style="font-weight: bold;">{{i.date.date}}  |  Event: {{i.event}}  |  Amount: {{i.amount}}  |  Saldo after movement: {{i.account_value_after}}</li>
        </ul>
        {% endfor %}
    
        <hr>
    
        <a href="{% url 'accounts:pay_form' %}">Insert new payment</a><br>
        <a href="{% url 'accounts:movements_form' %}">Move to own account</a><br>
        
    </body>
   
    
    </html> -->
    
    
    
    
    
    


--------          