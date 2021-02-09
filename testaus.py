
	<head>
		<title>OTH-Omataloushallinta</title>
		<meta charset="utf-8">
		<meta name= "viewport" content= "width=device-width, initial-scale=1.0"> 
		<link rel="stylesheet" type="text/css" href="{% static 'CSS/styles.css' %}">   
		<link rel="stylesheet" type="text/css" href="{% static ' font-awesome-4.7.0/css/font-awesome.min.css' %}">
		<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
		<link rel="preconnect" href="https://fonts.gstatic.com/"> 
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
		<script src="https://kit.fontawesome.com/a076d05399.js"></script>
	</head> 
    
<!DOCTYPE html>
<html>    
<head>
	<title>Luo tili</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">
   
	<style>
		
		.user_card {
            width: 350px;
            height: 820px;
			margin-top: 5px;
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

        .justify-content-center h3{
            margin-top: -50px;
        }

        .libele{
            color: azure;
        }


	</style>



</head>
<body>
	<div class="container h-100">
		<div class="d-flex justify-content-center h-100">
			<div class="user_card">
				<div class="d-flex justify-content-center">
                    
                         <h3 id="form-title">Luo tili </h3>
                    
				</div>
				   <div class= 'libele'>
                        <form action="/create_account/" method="POST" ,="" enctype="multipart/form-data">
                           
                            <input type="hidden" name="csrfmiddlewaretoken" value="lSURBeNoV0AJ3ZjyhhONNT6b0w4wc3o8JxT4eTsMnj8FyVHmCICoGXolTni5Q2Mh">
                            {% csrf_token %}
                       

              
                        <tr><th><label for="id_user">User:</label></th><td><select name="user" required id="id_user">
                        
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
                            <hr>
                        
                        <input type="submit" class="btn btn-primary" value="Save">
                        </form>
                </div>
 
            </div>

        </div>


    </div>

</div>
</div>


















                         <input type="hidden" name="csrfmiddlewaretoken" value="lSURBeNoV0AJ3ZjyhhONNT6b0w4wc3o8JxT4eTsMnj8FyVHmCICoGXolTni5Q2Mh"> 
                            {% csrf_token %}
                       

             
                       <tr><th><label for="id_user">User:</label></th><td><select name="user" required id="id_user">
                        
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
                            <hr>
                        
                        <input type="submit" class="btn btn-primary" value="Save">
                        </form>
                </div>
 
            </div>

        </div>


    </div>

</div>
</div>




sdfsd sdf sdf sdf dsf sdf 
as as
