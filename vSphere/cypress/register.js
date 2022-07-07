/// <reference types="cypress" />

describe('Register', () => {
    it('should register a new user', () => {
        const username = 'testuser'
        const password = 'testpassword'

        cy.visit('http://localhost:3000')
        cy.contains('a.nav-link','Register').click()
        cy.get('[data-cy=username]').type(username)
        cy.get('[data-cy=password]').type(password)
        cy.get('form').submit()
    });

    it ('should login a user', () => {
        const username = 'testuser'
        const password = 'testpassword'

        cy.visit('http://localhost:3000')
        cy.contains('a.nav-link','Login').click()
        cy.get('[data-cy=username]').type(username)
        cy.get('[data-cy=password]').type(password)
        cy.get('form').submit()
    });
    
})

    
