/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
const fs = require('fs');
const path = require('path');

exports.up = function(knex) {
  const filePath = path.join(__dirname, './sql/v1_init_db.sql');
  const sql = fs.readFileSync(filePath, 'utf8');
  return knex.raw(sql);
};

/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
exports.down = function(knex) {
  
};
