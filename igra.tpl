<!DOCTYPE html>
<html>

<body>
  <h1>Tri v vrsto</h1>

  <table border="5">
    <tr>
      <td>
      <form action="/place/0">   
        <input type="image" src="/static/{{ime0}}" name="ime0"value="0" class="btTxt submit" id="but0" />
       </form>              
      </td>
      <td>
              <form action="/place/1">      
            <input type="image" src="/static/{{ime1}}" name="ime1"value="1" class="btTxt submit" id="but1" />
            </form>
      </td>
      <td>
            <form action="/place/2">   
            <input type="image" src="/static/{{ime2}}" name="ime2"value="2" class="btTxt submit" id="but2" />
            </form>
      </td>
    </tr>
    <tr>
        <td>
            <form action="/place/3">   
              <input type="image" src="/static/{{ime3}}" name="ime3"value="3" class="btTxt submit" id="but3" />
              </form>
        </td>
        <td>
            <form action="/place/4">   
              <input type="image" src="/static/{{ime4}}" name="ime4"value="4" class="btTxt submit" id="but4" />
              </form>
        </td>
        <td>
            <form action="/place/5">   
              <input type="image" src="/static/{{ime5}}" name="ime5"value="5" class="btTxt submit" id="but5" />
              </form>
        </td>
      </tr>
      <tr>
        <td>
          <form action="/place/6">   
              <input type="image" src="/static/{{ime6}}" name="ime6"value="6" class="btTxt submit" id="but6" />
              </form>
        </td>
        <td>
          <form action="/place/7">   
              <input type="image" src="/static/{{ime7}}" name="ime7"value="7" class="btTxt submit" id="but7" />
              </form>
        </td>
        <td>
         <form action="/place/8">   
              <input type="image" src="/static/{{ime8}}" name="ime8"  value="8" class="btTxt submit" id="but8"/>
              </form>
        </td>
      </tr>
  </table>
 
  

    <form action="/AI_learns/">
      <input type="image"  src="/static/aivsai.png" class="btTxt submit" />
      </form>

      <h4>Zmag: {{win}}</h4>
      <h4>Zgub: {{lose}}</h4>
      <h4>Izenačenj: {{pat}}</h4>

    


 


</body>

</html>