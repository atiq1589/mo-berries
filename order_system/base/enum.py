from enum import Enum, IntEnum


class BaseEnum(Enum):
  """
  This is the base class for Enum Type
  It will define default functionality so that every Enum class does
  not need to redefine those
  """
  @classmethod
  def to_tuple(cls):
    return [(e.value, e.name) for e in cls]
