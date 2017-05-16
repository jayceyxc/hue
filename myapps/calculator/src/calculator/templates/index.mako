<%!from desktop.views import commonheader, commonfooter %>
<%namespace name="shared" file="shared_components.mako" />

${commonheader("Calculator", "calculator", user, request) | n,unicode}
## ${shared.menubar(section='mytab')}

## Use double hashes for a mako template comment
## Main body

<div class="container-fluid">
 % if op:
  <span>${a} ${op} ${b} = ${result}</span>
 % endif
 <form action=${url("calculator.views.index")} method=POST>
  ${ csrf_token(request) | n,unicode }
  <input name="a">
  <input type="radio" name="op" value="add" />+
  <input type="radio" name="op" value="subtract"/>-
  <input type="radio" name="op" value="multiply"/>*
  <input type="radio" name="op" value="divide"/>/
  <input name="b">
  <input type="submit" value="Calculate">
  </form>
</div>
${commonfooter(request, messages) | n,unicode}
