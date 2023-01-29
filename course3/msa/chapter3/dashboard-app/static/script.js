$(document).ready(function () {
  const ctx = document.getElementById('myChart');

  var label = []
  var data = []

  $.ajax({
    url: "/dashboard/statistics",
    method: "GET",
    dataType: "json"
  })
    .done(function (items) {
      for (var item of items) {
        label.push(item.created)
        data.push(item.count)
      }

      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: label,
          datasets: [{
            label: "Count of order",
            data: data,
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    })



  var ws = new WebSocket("ws://localhost:8080/dashboard/ws");
  ws.onmessage = function (target) {
    print(target)
    data = target.data.split("'")[1]
    order = JSON.parse(data)

    for (var item of data) {
      if (item.created == target.created)
        item[i].count = count++

      ctx.update()
    }
  };
})