function dragMoveListener (event) {
  var target = event.target,
      // keep the dragged position in the data-x/data-y attributes
      x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
      y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

  // translate the element
  target.style.webkitTransform =
  target.style.transform =
    'translate(' + x + 'px, ' + y + 'px) ';
    
  target.style.position ='absolute ';

  // update the posiion attributes
  target.setAttribute('data-x', x);
  target.setAttribute('data-y', y);
  target.style.height ='200px';
  target.style.width ='200px';
} 

dataCard = [];
interact('.dropzone').dropzone({
  // only accept elements matching this CSS selector
  accept: '.drag-drop',
  // Require a 75% element overlap for a drop to be possible
  overlap: 0.75,

  // listen for drop related events:

  ondropactivate: function (event) {
    // add active dropzone feedback
    event.target.classList.add('drop-active');
  },
  ondragenter: function (event) {
    var draggableElement = event.relatedTarget,
        dropzoneElement = event.target;

    // feedback the possibility of a drop
    dropzoneElement.classList.add('drop-target');
    draggableElement.classList.add('can-drop');
    
  },
  ondragleave: function (event) {
    // remove the drop feedback style
    event.target.classList.remove('drop-target');
    event.relatedTarget.classList.remove('can-drop');
    event.relatedTarget.removeAttribute('data-x');
    event.relatedTarget.removeAttribute('data-y');
    event.relatedTarget.removeAttribute('style');
    idCard = event.relatedTarget.id;
    dataCard.pop(idCard);

    console.log(dataCard);
  },
  ondrop: function (event) {
    //event.relatedTarget.textContent = 'Dropped';
    console.log("dropped");
    idCard = event.relatedTarget.id;
    dataCard.push(idCard);
    
    
    console.log("dataCard",dataCard);

     
  },
  ondropdeactivate: function (event) {
    // remove active dropzone feedback
    event.target.classList.remove('drop-active');
    event.target.classList.remove('drop-target');
  }
});

interact('.drag-drop')
  .draggable({
    allowFrom: '',
    inertia: true,
    /*restrict: {
      restriction: "parent",
      endOnly: true,
      elementRect: { top: 0, left: 0, bottom: 1, right: 1 }
  },*/
    autoScroll: true,
    onmove: dragMoveListener,
  });

  function getCookie(c_name)
  {
      if (document.cookie.length > 0)
      {
          c_start = document.cookie.indexOf(c_name + "=");
          if (c_start != -1)
          {
              c_start = c_start + c_name.length + 1;
              c_end = document.cookie.indexOf(";", c_start);
              if (c_end == -1) c_end = document.cookie.length;
              return unescape(document.cookie.substring(c_start,c_end));
          }
      }
      return "";
   }
   
 $(document).ready(function(){
  
    $( '#submit' ).click(function() {
      console.log('submit ok');
      deck_name = $("#deck_name").val();
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    $.ajax({
      type: 'POST',
      url: '/card/create/deck/',
      data: { 'deck' : dataCard, 'deck_name' : deck_name },
      success: function (data) {          
          alert("data send success");          
      }
    }); 
  });
  $( '#clean' ).click(function() {
    console.log('clean');
    var clear = document.getElementsByClassName("can-drop");
    for(var i = 0; i < clear.length; i++){
      clear[i].removeAttribute("style"); 
   }

   dataCard =[];

    console.log(dataCard);
    

});
 });