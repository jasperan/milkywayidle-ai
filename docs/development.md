# Development Guide

This guide provides information for developers who want to contribute to the Milky Way Idle AI Assistant project.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Ollama
- Basic understanding of:
  - Streamlit
  - LLaVA models
  - Image processing
  - Python development

### Setting Up Development Environment
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/milkywayidle-ai.git
   cd milkywayidle-ai
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

## Project Structure
```
milkywayidle-ai/
├── app.py              # Main application
├── requirements.txt    # Production dependencies
├── requirements-dev.txt # Development dependencies
├── docs/              # Documentation
│   ├── README.md      # Documentation index
│   ├── getting-started.md
│   ├── features.md
│   ├── user-guide.md
│   ├── technical.md
│   ├── faq.md
│   └── development.md
├── data/              # Data storage
├── tests/             # Test suite
└── .github/           # GitHub configurations
```

## Development Workflow

### 1. Creating a New Feature
1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes
3. Write tests
4. Update documentation
5. Submit a pull request

### 2. Testing
1. Run unit tests:
   ```bash
   pytest tests/
   ```

2. Run integration tests:
   ```bash
   pytest tests/integration/
   ```

3. Run performance tests:
   ```bash
   pytest tests/performance/
   ```

### 3. Documentation
1. Update relevant documentation files
2. Follow the existing style
3. Include code examples
4. Add diagrams if needed

## Code Style

### Python Style Guide
- Follow PEP 8
- Use type hints
- Write docstrings
- Keep functions focused

### Example
```python
def process_screenshot(image: Image.Image) -> dict:
    """
    Process a screenshot and extract game information.
    
    Args:
        image: PIL Image object of the screenshot
        
    Returns:
        dict: Extracted game information
    """
    # Implementation
    pass
```

## Testing

### Unit Tests
- Test individual components
- Mock external dependencies
- Cover edge cases
- Use pytest fixtures

### Integration Tests
- Test component interactions
- Use real Ollama instance
- Test full workflows
- Include error cases

### Performance Tests
- Measure response times
- Test resource usage
- Benchmark analysis
- Stress testing

## Contributing

### Pull Request Process
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

### Code Review
- Follow the style guide
- Include tests
- Update documentation
- Address feedback

### Commit Messages
- Use present tense
- Be descriptive
- Reference issues
- Follow convention

## Building and Deployment

### Local Build
1. Install dependencies
2. Run tests
3. Build documentation
4. Verify functionality

### Release Process
1. Update version
2. Update changelog
3. Run all tests
4. Create release tag
5. Build distribution
6. Upload to PyPI

## Debugging

### Common Issues
1. Model Connection
   - Check Ollama status
   - Verify model availability
   - Check network settings

2. Screenshot Capture
   - Verify permissions
   - Check monitor setup
   - Test capture manually

3. Performance
   - Profile code
   - Check resource usage
   - Monitor memory

### Debug Tools
- Python debugger
- Streamlit debug mode
- Logging system
- Performance profiler

## Maintenance

### Regular Tasks
1. Update dependencies
2. Run security checks
3. Update documentation
4. Review issues

### Version Updates
1. Check compatibility
2. Update requirements
3. Test thoroughly
4. Update documentation

## Roadmap

### Short Term
- [ ] Customizable intervals
- [ ] Achievement tracking
- [ ] Resource optimization
- [ ] Export functionality

### Long Term
- [ ] Machine learning predictions
- [ ] Advanced analytics
- [ ] Plugin system
- [ ] API integration

## Support

### Getting Help
- Check documentation
- Review issues
- Join Discord
- Contact maintainers

### Reporting Issues
1. Check existing issues
2. Create new issue
3. Provide details
4. Include logs

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details. 