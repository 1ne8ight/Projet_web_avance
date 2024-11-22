// SIDEBAR TOGGLE

// var sidebarOpen = false;
// var sidebar = document.getElementById("sidebar");

// function openSidebar() {
//   if (!sidebarOpen) {
//     sidebar.classList.add("sidebar-responsive");
//     sidebarOpen = true;
//   }
// }

// function closeSidebar() {
//   if (sidebarOpen) {
//     sidebar.classList.remove("sidebar-responsive");
//     sidebarOpen = false;
//   }
// }

// script.js
document.addEventListener("DOMContentLoaded", function () {
  // Récupérez les données transmises depuis Flask
  fetch("/graphique_affaire")
    .then((response) => response.json())
    .then((data) => {
      // Manipulez les données et effectuez l'affichage ici
      var mois = data.map((item) => item.mois);
      var sommeTotal = data.map((item) => item.somme_total);
      // Configuration du graphique à barres avec ApexCharts
      var barChartOptions = {
        chart: {
          type: "bar",
          height: 350,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: "55%",
            endingShape: "rounded",
          },
        },
        dataLabels: {
          enabled: false,
        },
        colors: ["#42a5f5"], // Couleur des barres
        series: [
          {
            data: sommeTotal, // Données du chiffre d'affaires
          },
        ],
        xaxis: {
          categories: mois, // Mois en tant que catégories de l'axe X
          title: {
            text: "Mois",
          },
        },
        yaxis: {
          title: {
            text: "Chiffre d'affaires",
          },
        },
      };

      // Création du graphique ApexCharts
      var barChart = new ApexCharts(
        document.querySelector("#bar-chart"),
        barChartOptions
      );
      barChart.render();
    })
    .catch((error) =>
      console.error("Erreur de récupération des données :", error)
    );
});

// AREACHART
document.addEventListener("DOMContentLoaded", function () {
  // Récupérez les données transmises depuis Flask
  fetch("/graphique_nbr_commande_mois")
    .then((response) => response.json())
    .then((data) => {
      // Manipulez les données et effectuez l'affichage ici
      var nom_du_mois = data.map((item) => item.nom_du_mois);
      var nombre_de_commandes = data.map((item) => item.nombre_de_commandes);

      var areaChartOptions = {
        series: [
          {
            name: "Purchase Orders",
            data: nombre_de_commandes,
          },
        ],
        chart: {
          height: 350,
          type: "area",
          // toolbar: {
          //   show: false,
          // },
        },
        colors: ["#4f35a1"],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
        },
        labels: nom_du_mois,
        markers: {
          size: 0,
        },
        yaxis: [
          {
            title: {
              text: "Nombre de commandes",
            },
          },
        ],
        tooltip: {
          shared: true,
          intersect: false,
        },
      };

      var areaChart = new ApexCharts(
        document.querySelector("#area-chart"),
        areaChartOptions
      );
      areaChart.render();
    })
    .catch((error) =>
      console.error("Erreur de récupération des données :", error)
    );
});

//-------------CHARTS POUR EMPLOYEES-------------
document.addEventListener("DOMContentLoaded", function () {
  // Récupérez les données transmises depuis Flask
  fetch("/graphique_commande_employe")
    .then((response) => response.json())
    .then((data) => {
      // Manipulez les données et effectuez l'affichage ici
      var employe = data.map((item) => item.employe);
      var commande = data.map((item) => item.commande);

      var options = {
        series: commande,
        chart: {
          type: "donut",
        },
        labels: employe,
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200,
              },
              legend: {
                position: "bottom",
              },
            },
          },
        ],
        title: {
          text: "Répartition des commandes par employé",
          align: "center",
        },
      };

      var chart = new ApexCharts(
        document.querySelector("#chartEmployes"),
        options
      );
      chart.render();
    })
    .catch((error) =>
      console.error("Erreur de récupération des données :", error)
    );
});

// ---------- CHARTS ----------

// BAR CHART
// var barChartOptions = {
//   series: [{
//     data: [10, 8, 6, 4, 2, 4, 76, 4, 2, 4, 7]
//   }],
//   chart: {
//     type: 'bar',
//     height: 350,
//     toolbar: {
//       show: false
//     },
//   },
//   colors: [
//     "#4f35a1",
//     "#246dec",
//     "#cc3c43",
//     "#4f35a1",
//     "#367952",
//     "#4f35a1",
//     "#f5b74f",
//     "#4f35a1",
//     "#4f35a1",
//     "#4f35a1",
//     "#4f35a1",
//     "#f5b74f",
//     "#4f35a1",
//     "#4f35a1",
//     "#4f35a1",
//   ],
//   plotOptions: {
//     bar: {
//       distributed: true,
//       borderRadius: 4,
//       horizontal: false,
//       columnWidth: '40%',
//     }
//   },
//   dataLabels: {
//     enabled: false
//   },
//   legend: {
//     show: false
//   },
//   xaxis: {
//     categories: ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Octobre", "Novembre", "Decembre"],
//   },
//   yaxis: {
//     title: {
//       text: "Chiffre d'affaire"
//     }
//   }
// };

// var barChart = new ApexCharts(document.querySelector("#bar-chart"), barChartOptions);
// barChart.render();

// AREA CHART
// var areaChartOptions = {
//   series: [
//     {
//       name: "Purchase Orders",
//       data: [31, 40, 28, 51, 42, 109, 100],
//     },
//     {
//       name: "Sales Orders",
//       data: [11, 32, 45, 32, 34, 52, 41],
//     },
//   ],
//   chart: {
//     height: 350,
//     type: "area",
//     toolbar: {
//       show: false,
//     },
//   },
//   colors: ["#4f35a1", "#246dec"],
//   dataLabels: {
//     enabled: false,
//   },
//   stroke: {
//     curve: "smooth",
//   },
//   labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
//   markers: {
//     size: 0,
//   },
//   yaxis: [
//     {
//       title: {
//         text: "Purchase Orders",
//       },
//     },
//     {
//       opposite: true,
//       title: {
//         text: "Sales Orders",
//       },
//     },
//   ],
//   tooltip: {
//     shared: true,
//     intersect: false,
//   },
// };

// var areaChart = new ApexCharts(
//   document.querySelector("#area-chart"),
//   areaChartOptions
// );
// areaChart.render();

// // Fonction pour charger et mettre à jour le contenu
// function chargerContenu() {
//   // Effectuez ici votre requête AJAX pour charger les données du serveur
//   // Par exemple, avec jQuery :
//   $.ajax({
//       url: '/dashboard',
//       method: 'GET',
//       success: function(data) {
//           // Mettez à jour le contenu de la page avec les données reçues
//           document.querySelector('#actif').innerHTML = data['actif'];
//       }
//   });
// }

// // Appelez la fonction toutes les X millisecondes (par exemple, toutes les 5 secondes)
// setInterval(chargerContenu, 5000); // 5000 millisecondes équivaut à 5 secondes

// const commandeCount = document.getElementById('commande-count');

// // Fonction pour mettre à jour le nombre de commandes
// function updateCommandeCount(count) {
//     document.getElementById('commande-count').innerText = count;
// }

// // Établir une connexion SSE pour recevoir les mises à jour en temps réel
// const eventSource = new EventSource('/sse');
// eventSource.onmessage = (event) => {
//     const count = JSON.parse(event.data).count;
//     updateCommandeCount(count);
// };
