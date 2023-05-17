const changetheme = document.querySelector(".b2");
const sidebar = document.querySelector(".div1");
const wholebar = document.querySelector(".div2")
const button = document.querySelectorAll(".b2");
const textColor = document.querySelectorAll("h1")

function darktheme () {
    
  wholebar.classList.toggle("darkmode1")
  sidebar.classList.toggle("darkmode");
    
    for (let item of button) {
      item.classList.toggle("darkmode");
    }
    for (let texts of textColor) {
        texts.classList.toggle("textcolor")
    }

}

changetheme.addEventListener("click", darktheme);


const changeText = () => {
  if (changetheme.textContent === "Dark Theme") {
    changetheme.textContent = "Light Theme";
  } else if (changetheme.textContent === "Light Theme") {
    changetheme.textContent = "Dark Theme";
  }
};
changetheme.addEventListener("click", changeText);