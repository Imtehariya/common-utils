from enum import Enum

class Status(Enum):
    INACTIVE = 0
    ACTIVE = 1
    PENDING = 2
    DELETED = 10

class UserType(str, Enum):
    INDIVIDUAL = 'individual'
    BUSINESS = 'business'

class UserRole(Enum):
    SUPER_ADMIN = 'super_admin'
    ADMIN = 'admin'
    VIEWER = 'viewer'
    CLIENT_ADMIN = 'client_admin'

class UserStep(str, Enum):  # Inheriting from `str` makes it work with FastAPI validation
    OTP = "otp"
    BUSINESS_INFO = "info"
    ID_VERIFICATION = "verification"
    SELFIE = "selfie"
    LIVENESS = "live"
    COMPLETE = "done"

class AccountType(str, Enum):
    CURRENCY = 'currency'
    SAVING = 'saving'
    
class PaymentExecutionStatus(str, Enum):
    NOW = 'now'
    SCHEDULED = 'schedule'

class PaymentStatus(Enum):
    DRAFT = 0
    PENDING = 1
    HISTORY = 2
    
class FeeType(Enum):
    ACCOUNT_ADMINISTRATION = 0
    PAYMENTS = 1
    ACCOUNTANCY = 2
    CASH_MANAGEMENT = 3
    
class FeeBillingFrequency(Enum):
    ONE_TIME = 0
    PER_HOUR = 1
    PER_MONTH = 2
    PER_YEARLY = 3
    SHARE = 4
    
class FeePriceType(Enum):
    NONE = 0
    FREE = 1
    CURRENCY = 2
    PERCENTAGE = 3
    SHARE = 4

class EntityType(str, Enum):
    DIRECTOR = 'director'
    SHAREHOLDER = 'shareholder'