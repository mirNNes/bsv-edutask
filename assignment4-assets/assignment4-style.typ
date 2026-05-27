#set page(
  paper: "a4",
  margin: (
    top: 36mm,
    bottom: 32mm,
    left: 30mm,
    right: 30mm,
  ),
)

#set text(
  font: "Arial",
  size: 10pt,
  fill: black,
)

#set par(
  leading: 0.58em,
  spacing: 0.9em,
)

#set list(
  marker: [-],
  indent: 0pt,
  body-indent: 0.65em,
  spacing: 0.45em,
)

#set table(
  stroke: 0.7pt + black,
  inset: (
    x: 5pt,
    y: 4.5pt,
  ),
  align: left,
)

#show table.cell: set table.cell(align: left)

#show heading.where(level: 1): it => {
  set text(size: 14pt, weight: "bold")
  block(above: 0pt, below: 1.2em, it)
}

#show heading.where(level: 2): it => {
  set text(size: 16pt, weight: "regular")
  block(above: 3.2em, below: 1.2em, it)
}

#show heading.where(level: 3): it => {
  set text(size: 13pt, weight: "regular")
  block(above: 1.8em, below: 0.8em, it)
}

#show figure: it => it.body

#show image: it => {
  block(above: 1.8em, below: 1.8em, width: 100%, it)
}
