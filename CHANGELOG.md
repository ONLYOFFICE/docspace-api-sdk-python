# Change Log

## 3.7.0

### Added

- Added new API methods and enhanced models with additional properties
- Added tag Rooms / Groups
- Added Apps API for managing portal applications
- Added Privacy Room API and encryption key management (encryption keys, file encryption info, file keys, access request keys, room privacy filter)
- Added per-user AI settings models
- Added AI model pricing models (chat, embedding, and image prices) and AI image model support
- Added AI credit balance request model
- Added customer usage reporting (monthly usage and service usage reports)
- Added subscription balance and upcoming payment models
- Added backups count result models
- Added external database sync task models
- Added generated file models
- Added external sharing settings models
- Added two-factor authentication confirmation data models
- Added user existence check models
- Added webhook trigger models
- Documented rate limiting response headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After`) and `429 Too Many Requests` responses across endpoints

### Changed

- Updated SDK OpenAPI specification v3.7.0
- Updated example values, added email length validation, and adjusted method return types in API models and methods
- Typed the `retries` client parameter as `urllib3.util.retry.Retry`
- Updated model fields and enums across the SDK

### Fixed

- Fixed & / ' issues

## 3.6.0

- Improved enum generation and data type consistency
- Updated API method descriptions and model fields
- SDK regenerated from OpenAPI specification v3.6.0
- Updated python models structure (modelAllOf fixes)
- Fixed reserved keyword conflict (`None` → `None_`)

## 3.5.1

- packaging with toml

## 3.5.0

- Initial release
