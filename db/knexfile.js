// Update with your config settings.

/**
 * @type { Object.<string, import("knex").Knex.Config> }
 */
require('dotenv').config();

module.exports = {

  development: {
    client: 'pg',
    connection: "postgres://postgres:admin_2024@localhost:5432/horario_onibus",
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      directory: './migrations',
      schemaName: 'quadro_horarios',
      tableName: 'knex_migrations'
    }
  },

  production: {
    client: 'pg',
    connection: process.env.CONNECTION_STRING_MIGRATION,
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      directory: './migrations',
      schemaName: 'online',
      tableName: 'knex_migrations'
    }
  }

};
