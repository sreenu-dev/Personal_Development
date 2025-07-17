using TaskManagementAPI.Data;
using TaskManagementAPI.DTOs;
using TaskManagementAPI.Models;

namespace TaskManagementAPI.Services
{
    public class TaskService : ITaskServices
    {
        private readonly AppDbContext _context;
        public TaskService(AppDbContext context)
        {
            _context = context;
        }
        private readonly List<TaskItem> tasks = new();
        private int _nextId = 1;
        public TaskItem Create(TaskItemDTO dto)
        {
            var task = new TaskItem
            {
                Id = _nextId++,
                Description = dto.Description,
                IsCompleted = dto.IsCompleted,
                Title = dto.Title
            };
            _context.TaskItems.Add(task);
            _context.SaveChanges();
            return task;
            
        }

        public bool Delete(int id)
        {
            var task = GetById(id);
            if (task == null)
            {
                return false;
            }
            _context.TaskItems.Remove(task);
            _context.SaveChanges();
            return true;
        }

        public List<TaskItem> GetAll()
        {
            return _context.TaskItems.ToList();
        }

        public TaskItem? GetById(int id)
        {
            return _context.TaskItems.Find(id);
        }
    }
}