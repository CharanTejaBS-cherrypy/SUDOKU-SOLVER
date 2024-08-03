document.addEventListener("DOMContentLoaded", () => {
  const cells = document.querySelectorAll(".cell");

  cells.forEach((cell) => {
    cell.addEventListener("input", () => {
      if (!/^[1-9]$/.test(cell.value)) {
        cell.value = "";
        alert("Invalid Input");
      }
    });
  });
});

function solveSudoku() {
  let grid = [];
  for (let i = 0; i < 9; i++) {
    let row = [];
    for (let j = 0; j < 9; j++) {
      let cell = document.getElementById(`cell-${i}-${j}`);
      row.push(cell.value === "" ? 0 : parseInt(cell.value));
      if (cell.value !== "") {
        cell.classList.add("user-input");
      }
    }
    grid.push(row);
  }

  fetch("/solve", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ grid: grid }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.valid) {
        let solution = data.solution;
        for (let i = 0; i < 9; i++) {
          for (let j = 0; j < 9; j++) {
            let cell = document.getElementById(`cell-${i}-${j}`);
            if (cell.value === "") {
              cell.value = solution[i][j] !== 0 ? solution[i][j] : "";
              cell.classList.add("solver-input");
            }
            // Reapply subgrid class to ensure colors are preserved
            cell.classList.add(
              `subgrid-${Math.floor(i / 3) * 3 + Math.floor(j / 3)}`
            );
          }
        }
      } else {
        alert("Invalid Input");
      }
    });
}

function clearBoard() {
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      let cell = document.getElementById(`cell-${i}-${j}`);
      cell.value = "";
      cell.classList.remove("user-input", "solver-input");
    }
  }
}
