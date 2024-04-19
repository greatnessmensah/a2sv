describe('full app testing', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should display Redux Fundamentals Example in the section', () => {
    cy.get('section').should('contain', 'Redux Fundamentals Example')
  })
  it('display Todos', () => {
    cy.get('section').should('contain', 'Todos')
  })
  it('should have an input field with the correct placeholder', () => {
    cy.get('input').should('have.attr', 'placeholder', 'What needs to be done?')
  })
  it('should contain multiple words in the footer', () => {
    cy.get('footer')
      .should('contain', 'Actions')
      .and('contain', 'Remaining Todos')
      .and('contain', 'Filter by Status')
      .and('contain', 'Filter by Color')
  })
  it("should add a todo", () => {
    cy.get('.new-todo').type('Learn Cypress{enter}')
    cy.get('.todo-list').should('contain', 'Learn Cypress')
  })
  it("should delete a task", () => {
    cy.get('.new-todo').type('Learn Cypress{enter}')
    cy.get('.todo-list').should('contain', 'Learn Cypress')
    cy.get('.destroy').last().click()
    cy.get('.todo-list').should('not.contain', 'Learn Cypress')
  })
  it("completes a task", () => {
    cy.get('.new-todo').type('Learn Cypress{enter}')
    cy.get('.todo-list').should('contain', 'Learn Cypress')
    cy.get('.toggle').last().click()
    cy.get('#root > div > main > section > div > footer > div.filters.statusFilters > ul > li:nth-child(2) > button').click()
    cy.get('.todo-list').should('not.contain', 'Learn Cypress')
  })
})
