let allBooks = [
  book 1 =
    {
    title: "harry potter",
    author: "rowling",
    image: [],
    alreadyread: true,
    },
  book 2 =
    {
    title: "lord of the rings",
    author: "rowling",
    image: [],
    alreadyread: true,
    }
  book 3 =
    {
    title: "people",
    author: "human",
    image: [],
    alreadyread: false,
    }
  book 4 =
    {
    title: "power",
    author: "greene",
    image: [],
    alreadyread: true
    }
}

function createTable() {
  let table = document.createElement("table");
  let row1 = document.createElement("tr");
  table.appendChild(row1);

  let head1 = document.createElement("th");
  head1.style.paddingRight = `80px`;
  let text1 = document.createTextNode("Title");
  head1.appendChild(text1);
  row1.appendChild(head1);

  let head2 = document.createElement("th");
  head2.style.paddingRight = `80px`;
  let text2 = document.createTextNode("Author");
  head2.appendChild(text2);
  row1.appendChild(head2);

  let head3 = document.createElement("th");
  let text3 = document.createTextNode("Image");
  head3.appendChild(text3);
  row1.appendChild(head3);

  document.body.appendChild(table);
}

for (let book of allBooks) {
  let bookRow = document.createElement(`tr`);
  table.appendChild(bookRow);

  let titleCol = document.createElement(`td`);
  bookRow.appendChild(titleCol);
  titleCol.innerHTML = book[`title`];
  titleCol.setAttribute('class', 'bookinfo');

  let authorCol = document.createElement(`td`);
  bookRow.appendChild(titleCol);
  titleCol.innerHTML = book[`author`];

  let picCol = document.createElement(`td`);
  let image = document.createElement(`img`);
  image.setAttribute(`src`, book[`image`]);
  image.style.width = `100px`;
  picCol.appendChild(image);
  bookRow.appendChild(picCol);

  if (book[`alreadyread`] == true) {
    bookRow.style.color = `red`;
  }
}
