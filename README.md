# Github Actions

### Run test without watching files
CI=true npm run test

### Test with coverage report
CI=true npm run test -- --coverage

### Build app into build folder
npm run build

### Surge - static web publishing
npm install --global surge
surge --domain scandalous-quilt.surge.sh

### prettier
npm install --save-dev --save-exact prettier
npx prettier --check "**/*.js"
npx prettier --write "**/*.js"

## Workflow
### Pull Request
- Install dependencies
- Check code formatting
- Run automated tests
- Upload code coverage as an artifact
- Cache dependencies

### Merge to Develop branch
- Install dependencies
- Check code formatting
- Run automated tests
- Upload code coverage as an artifact
- Build project
- Upload build as an artifact
- Deploy to staging server
- Cache dependencies

### Merge Develop into Master
- Install dependencies
- Check code formatting
- Run automated tests
- Upload code coverage as an artifact
- Build project
- Create a release
- Deploy to prod server
- Upload coverage to codecov

### Actions
- Job failure -> create issue
- Issue created -> send slack message
- Release created -> send slack message
