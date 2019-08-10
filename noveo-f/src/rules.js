import { Validator } from 'vee-validate'

// custom selector rules

function unique_user(value, objects) {
  const filter = objects.filter((el) => {
    return value === el.email
  })
  if (filter.length > 0) {
    return false
  }
  return true
}


const rules = {
  unique_user: (value, objects) => {
    return unique_user(value, objects)
  },
}
export default(validator) => {
  Object.keys(rules).forEach(rule => {
    validator.extend(rule, rules[rule])
  })
}
