from .math_utils import add, multiply
from .text_utils import reverse_string

function_registry = {
    "Add Numbers": add,
    "Multiply Numbers": multiply,
    "Reverse String": reverse_string
}
