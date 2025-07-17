using Microsoft.AspNetCore.Mvc;
using TaskManagementAPI.DTOs;
using TaskManagementAPI.Services;

namespace TaskManagementAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TaskController : ControllerBase
    {
        private readonly ITaskServices _taskService;

        public TaskController(ITaskServices taskServices)
        {
            _taskService = taskServices;
        }

        [HttpGet]
        public IActionResult GetAll()
        {
            return Ok(_taskService.GetAll());
        }

        [HttpGet]
        [Route("GetAll")]
        public IActionResult GetAllOne() => Ok(_taskService.GetAll());

        [HttpGet("{id}")]
        public IActionResult Get(int id)
        {
            var task = _taskService.GetById(id);
            if (task == null) return NotFound();
            return Ok(task);
        }

        [HttpPost]
        public IActionResult Create([FromBody] TaskItemDTO dto)
        {
            var task = _taskService.Create(dto);
            return CreatedAtAction(nameof(Get), new { id = task.Id }, task);
        }

        [HttpDelete]
        public IActionResult Delete(int id)
        {
            var deleted = _taskService.Delete(id);
            if (!deleted) return NotFound();
            return NoContent();
        }
    }
}
