describe('Simple Todo Tests (R8)', () => {

  let email

  before(function () {
    cy.fixture('user.json').then((user) => {
      email = user.email

      cy.request({
        method: 'POST',
        url: 'http://localhost:5001/users/create',
        form: true,
        body: user
      })
    })
  })

  beforeEach(function () {
    cy.visit('http://localhost:3001')

    // login
    cy.contains('div', 'Email Address')
      .find('input[type=text]')
      .type(email)

    cy.get('form').submit()

    // skapa task
    cy.get('input[placeholder="Title of your Task"]')
      .type('Test Task')

    cy.get('input[placeholder^="Viewkey"]')
      .type('dQw4w9WgXcQ')

    cy.get('input[value="Create new Task"]').click()

    // öppna task
    cy.contains('Test Task').click()
  })

  it('Create todo', () => {
    cy.get('input[placeholder="Add a new todo item"]')
      .type('My first todo', { force: true })

    cy.get('input[value="Add"]').click({ force: true })

    cy.contains('My first todo')
      .should('exist')
  })

  it('Toggle todo', () => {
    cy.get('input[placeholder="Add a new todo item"]')
      .type('Toggle todo', { force: true })

    cy.get('input[value="Add"]').click({ force: true })

    cy.contains('Toggle todo')
      .parent()
      .find('.checker')
      .click({ force: true })

    cy.contains('Toggle todo')
      .parent()
      .find('.checker')
      .should('have.class', 'checked')
  })

  it('Delete todo', () => {
    cy.get('input[placeholder="Add a new todo item"]')
      .type('Delete todo', { force: true })

    cy.get('input[value="Add"]').click({ force: true })

    cy.contains('Delete todo')
      .parent()
      .find('.remover')
      .click({ force: true })

    cy.wait(1000)

    cy.contains('Delete todo')
    .should('not.exist')
  })

})
