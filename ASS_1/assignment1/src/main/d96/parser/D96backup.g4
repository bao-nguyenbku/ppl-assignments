// @lexer::header {
// from lexererr import *
// import inspect
// }

// @lexer::members {
// def emit(self):
//     tk = self.type
//     result = super().emit()
//     print('----------------------------------------------------------------------------')
//     attributes = inspect.getmembers(D96Lexer, lambda a:not(inspect.isroutine(a)))
//     user_defined_attr = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
//     for i in user_defined_attr:
//         if tk == i[1]:
//             print ("{:<30} {:<30} {:<50}".format(result.text, '|', i[0]))
//     print('----------------------------------------------------------------------------')
//     if tk == self.INTEGER_LITERAL or tk == self.REAL_LITERAL or tk == self.ARRAY_SIZE:
//         result.text = result.text.replace('_', '')
//     return result
// }