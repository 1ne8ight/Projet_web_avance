
  // Fonction pour gérer le clic sur les liens
  function gestionClicLien(event) {
      // Désactive tous les liens
      var tousLesLiens = document.querySelectorAll('li a');
      for (var i = 0; i < tousLesLiens.length; i++) {
          tousLesLiens[i].classList.remove('active-link');
      }

      // Active le lien cliqué
      event.target.classList.add('active-link');
  }

  // Ajoute un gestionnaire de clic à chaque lien
  var tousLesLiens = document.querySelectorAll('li a');
  for (var i = 0; i < tousLesLiens.length; i++) {
      tousLesLiens[i].addEventListener('click', gestionClicLien);
      
      // Ajoute la classe active-link pour le lien correspondant à la page actuellement visitée
      if (window.location.href === tousLesLiens[i].href) {
          tousLesLiens[i].classList.add('active-link');
      }
  }
