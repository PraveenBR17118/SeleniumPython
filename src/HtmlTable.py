'''
Created on 20-Jan-2020

@author: praveen
'''
f = open('Sample.html','w')

message = """<html>
<html>
<table border="3" bordercolor="330000" style="background-color:#FFFFFF" width="25%" cellpadding="1" cellspacing="0" font size="50">
<tbody>
 <tr>
  <th>Product</th>
  <th>Article</th>
  <th>Price</th>
 </tr>
 <tr>
  <td>Product1</td>
  <td>0001</td>
  <td>10</td>
 </tr>
 <tr>
  <td>Product2</td>
  <td>0002</td>
  <td>15</td>
 </tr>
 <tr>
  <td>Product3</td>
  <td>0003</td>
  <td>12</td>
 </tr>
 <tr>
  <td>Product4</td>
  <td>0004</td>
  <td>20</td>
 </tr>
</tbody>
 </table>
</html>"""

f.wrte(message)
f.close()