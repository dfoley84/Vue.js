/// <reference types="cypress" />

describe('Test Suite', () => {
    it('test URL', () => {
        cy.visit('http://localhost:3000/')
    });
    it('Test Login', () => {
        cy.contains('a.nav-link', 'Login').click()
    })
})
